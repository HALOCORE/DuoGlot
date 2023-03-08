import cython
import sys
if cython.compiled: print("[grammar_expand] Compiled.", file=sys.stderr)
else: print("[grammar_expand] Interpreted.", file=sys.stderr)
####################################

import traceback
import timeit
import grammar_dlmparser as gdp
import grammar_rules
import consts
from consts import DEBUG_VERBOSE, NormalException, UnderstoodException
import copy 
import ast_pretty
import sys



################################################################### 
TRANS_VERBOSE : cython.int = DEBUG_VERBOSE

class TransSession():
  def __init__(self, source_code, source_ast, source_ann, source_language_name, target_language_name, target_grammar, program_str, optional_dbg_info_save_func, slot_dedup_enabled):
    self._BACKWARD_MAX_STEP : cython.int = 5
    self._SNAPSHOT_INTERVAL : cython.int = 800
    self._SLOT_DEDUP_ENABLED : cython.bint = slot_dedup_enabled
    # the slot_dedup is only enabled for astnode choices for now.
    # step choices cannot use slot_dedup unless the cache is not on slots, but on slots' ranges.
    # current impl caches a one-to-one mapping from ranges to slots.
    # Okay to expose 
    self.source_code = source_code
    self.source_ast = source_ast
    self.source_ann = source_ann
    self.source_language_name = source_language_name
    self.target_language_name = target_language_name
    self.target_grammar = target_grammar
    self.expansion_programs = []  # a list of expansion programs
    self.program_dbg_info = {
      "expansion_programs": []
    }
    # internals
    self._optional_dbg_info_save_func = optional_dbg_info_save_func
    self._counter_expansion_id : cython.int = 0
    self._counter_slot_id : cython.int = 1
    self._counter_alt_id : cython.int = 1
    self._slot_dict = {0: gdp.Slot(0, None, ([self.source_ast], 0, 1))}
    self._slot_dedup_lookup = {}
    self.__slot_expand_info_dict = {} # no direct access
    self._alt_tree_dict = {
      0: self._alt_node(
        0, 0, None, None, None, [0], 
        {"count": 0, "done": False}, {}, False, True)
    }   # alt_id -> alt_node
    self._alt_parser_result_dict = {}
    
    self._alt_parser_dict = {
      0: gdp.DelimitedParser(None, self._slot_dict[0].slot_id, target_grammar["_initial_prod"], target_grammar, self.target_language_name, self._optional_dbg_info_save_func)
    } # alt_id -> Parser
    self.any_error = False
    self._set_program_str(program_str)

  def _alt_calc_todo_slots(self, expansion: gdp.Expansion, prev_alt_node):
    # todo slot dedup impl here? If dedup is on for the whole transsession, then this expansion and its corresponding slot must be unique. 
    # can unique expansion/slot produce duplicated children slots? Should be yes. 
    # But can the duplicated children slots appear in the same transduction history? 
    # (only slots/expansions along a specific transduction history is book-keeped in transducer)
    # Not possible in current transducer impl. because matches inside an expansion are exclusive.
    # If matches are not exclusive, [1] + 2   and [1 +] 2 can be slot 1:([1]) slot 2:([1 +]). Another expansion on slot 2 break it down to [1] and [+] 
    # will be unaware that [1] is already handled. 
    # If we keep duplicated todo slots, will they affect the transduction?
    old_todo_slot_ids = prev_alt_node["todo_slot_ids"]
    prepend_ids = [x.slot_id for x in expansion.slots if x is not None]
    return prepend_ids + old_todo_slot_ids[1:]

  def _alt_node(self, 
    alt_id, alt_step, 
    expansion, choose_idx, prev_alt_id, todo_slot_ids, next_choices_status, next_alt_choose_dict, is_all_rejected, is_checkpoint):
    return {
      "alt_id": alt_id,
      "alt_step": alt_step,
      "expansion": expansion,
      "choose_idx": choose_idx,
      "prev_alt_id": prev_alt_id,
      "todo_slot_ids": todo_slot_ids,
      "next_choices_status": next_choices_status, 
      "next_alt_choose_dict": next_alt_choose_dict,
      "is_all_rejected": is_all_rejected,
      "is_checkpoint": is_checkpoint
    }

  def _parser_result(self,
    is_acceptable, is_done, is_error, dbg_info, stuck_slot_id):
    return {
      "is_acceptable": is_acceptable,
      "is_done": is_done,
      "is_error": is_error,
      "dbg_info": dbg_info,
      "stuck_slot_id": stuck_slot_id,
    }
  
  def _fetch_parser(self, alt_id):
    """assume the parsing result of alt_id is already available. We don't care. Return a parser"""
    assert alt_id == 0 or alt_id in self._alt_parser_result_dict
    alt_node = self._alt_tree_dict[alt_id]
    if alt_id in self._alt_parser_dict and self._alt_parser_dict[alt_id] is not None:
      if alt_node["is_checkpoint"]:
        print("# _fetch_parser cloning from checkpoint:", alt_id)
        return self._alt_parser_dict[alt_id].clone()
      else:
        parser = self._alt_parser_dict[alt_id]
        self._alt_parser_dict[alt_id] = None
        return parser
    else:
      assert not alt_node["is_checkpoint"]
      prev_id = alt_node["prev_alt_id"]
      if prev_id is None: assert False
      expansion = alt_node["expansion"]
      fetched_parser = self._fetch_parser(prev_id)
      is_accepted, _ = fetched_parser.add_expansion_parse_until_stuck(expansion)
      assert is_accepted
      assert fetched_parser.last_time_stuck_slot_id == self._alt_parser_result_dict[alt_id]["stuck_slot_id"]
      return fetched_parser
    
  def _update_alt_node_as_checkpoint(self, alt_id):
    alt_node = self._alt_tree_dict[alt_id]
    if alt_node["is_checkpoint"]: return
    parser = self._fetch_parser(alt_id)
    self._alt_parser_dict[alt_id] = parser
    alt_node["is_checkpoint"] = True
    print(f"!!! Updating (alt_id:{alt_id}) as checkpoint.")
    

  def _encure_parser_result(self, alt_node):
    # make sure the parser result is set. 
    # notice: parser_result might be error
    alt_id = alt_node["alt_id"]
    if alt_id in self._alt_parser_result_dict: 
      return self._alt_parser_result_dict[alt_id]
    else:
      try:
        # fetch the previous parser (move or clone from the last checkpoint and move) and run it
        prev_alt_id = alt_node["prev_alt_id"]
        fetched_parser = self._fetch_parser(prev_alt_id)
        expansion = alt_node["expansion"]
        is_accepted, dbg_info = fetched_parser.add_expansion_parse_until_stuck(expansion)
        parser_result = self._parser_result(
          is_accepted, fetched_parser.last_time_parsing_done, 
          False, dbg_info, fetched_parser.last_time_stuck_slot_id)
        self._alt_parser_result_dict[alt_id] = parser_result
        self._alt_parser_dict[alt_id] = fetched_parser
        return parser_result
      except Exception as err:
        print("#################### _encure_parser_result FAILED! ####################")
        self.any_error = True
        fetched_parser.dbg_print_tail_stack()
        err_dbg_info = fetched_parser._dbg_info_finish_for_ex_error()
        err_parser_result = self._parser_result(
          False, False, True, err_dbg_info, None)
        self._alt_parser_result_dict[alt_id] = err_parser_result
        raise err

  def _get_alt_partial_ast(self, alt_node):
    alt_id = alt_node["alt_id"]
    assert alt_id in self._alt_parser_dict
    parser = self._alt_parser_dict[alt_id]
    elem_list = parser.get_current_elem_list()
    return ast_pretty.elem_list_to_mapanno_ast(elem_list)

  def _get_alt_debug_history(self, alt_node):
    # get dbg_debug_info from the chain of parents start from alt_node
    alt_debug_history = []
    while alt_node["alt_id"] != 0:
      alt_id = alt_node["alt_id"]
      dbg_info = self._alt_parser_result_dict[alt_id]["dbg_info"]
      range_cursor = self._slot_dict[alt_node["expansion"].corres_slot_id].range_cursor
      alt_step = alt_node["alt_step"]
      range_info = None
      if alt_step == 1:
        assert len(range_cursor[0]) == 1
      else:
        range_info = (range_cursor[0][1], range_cursor[1], range_cursor[2])
      alt_debug_history.append({
        "alt_step": alt_step,
        "range_info": range_info,
        "next_choices_status": alt_node["next_choices_status"] , 
        "dbg_info": dbg_info
      })
      alt_node = self._alt_tree_dict[alt_node["prev_alt_id"]]
    alt_debug_history = list(reversed(alt_debug_history))
    return alt_debug_history
    
  def _get_or_create_alt_node(self, prev_alt_node, slot_expan_idx):
    if TRANS_VERBOSE > -10: print(f"_get_or_create_alt_node (prev_id:{prev_alt_node['alt_id']}) (se_idx:{slot_expan_idx}) ...")
    assert len(prev_alt_node["todo_slot_ids"]) > 0
    prev_alt_node_id = prev_alt_node["alt_id"]
    prev_alt_step = prev_alt_node["alt_step"]
    new_node_corres_slot_id = prev_alt_node["todo_slot_ids"][0]
    if not slot_expan_idx in prev_alt_node["next_alt_choose_dict"]:
      expansion = self._get_expansion_for_slot(new_node_corres_slot_id, slot_expan_idx)
      # TODO: discriminate No expansion and bad selection. Or should this be handled by frontend? TODO.
      if expansion is None: raise NormalException(f"No expansion for the chosen/default index slot_id:{new_node_corres_slot_id} with idx:{slot_expan_idx}")
      next_choices_status = self._get_expansions_stat_for_slot(new_node_corres_slot_id)
      assert "next_choices_status" in prev_alt_node
      prev_alt_node["next_choices_status"] = next_choices_status
      alt_node = self._alt_node(
        self._counter_alt_id, 
        prev_alt_step + 1,
        expansion, slot_expan_idx,
        prev_alt_node_id, 
        self._alt_calc_todo_slots(expansion, prev_alt_node),
        {"count": 0, "done": False}, {}, False, False)
      self._alt_tree_dict[alt_node["alt_id"]] = alt_node
      prev_alt_node["next_alt_choose_dict"][slot_expan_idx] = alt_node["alt_id"]
      self._counter_alt_id += 1
    return self._alt_tree_dict[prev_alt_node["next_alt_choose_dict"][slot_expan_idx]]

  def _create_or_get_slot(self, belong_ex_id, range_cursor):
    ast_id = range_cursor[0][1]
    assert isinstance(ast_id, int)
    start_idx = range_cursor[1]
    end_idx = range_cursor[2]

    if self._SLOT_DEDUP_ENABLED:
      astid_dict = None
      if ast_id in self._slot_dedup_lookup:
        astid_dict = self._slot_dedup_lookup[ast_id]
        if (start_idx, end_idx) in astid_dict:
          return astid_dict[(start_idx, end_idx)]
      else:
        astid_dict = {}
        self._slot_dedup_lookup[ast_id] = astid_dict

    self._counter_slot_id += 1
    new_slot = gdp.Slot(self._counter_slot_id, belong_ex_id, range_cursor)
    self._slot_dict[self._counter_slot_id] = new_slot
    
    if self._SLOT_DEDUP_ENABLED:
      # add to cache
      astid_dict[(start_idx, end_idx)] = new_slot

    return new_slot

  def _create_expansion(self, corres_slot_id, m_expand, matching_ids, slot_cursors, matching_values, matching_strs, matching_anynts, matching_liststrs, matching_annos, notes=None):
    self._counter_expansion_id += 1
    return gdp.Expansion(
      self._counter_expansion_id, 
      corres_slot_id, 
      m_expand, 
      matching_ids,
      slot_cursors,
      matching_values,
      matching_strs,
      matching_anynts,
      matching_liststrs,
      matching_annos,
      lambda ex_id, cursor : self._create_or_get_slot(ex_id, cursor),
      notes)
    
  def _possible_expansion_iter_gen(self, slot):
    if TRANS_VERBOSE > 0: print(f"_possible_expansion_iter_gen slot: ({slot})")
    choose_idx = 0
    for rule_id in range(len(self.expansion_programs)):
      me_prog = self.expansion_programs[rule_id]
      ruletype = me_prog["type"]
      match = me_prog["match"]
      expand = me_prog["expand"]
      flag_dict = me_prog["flags"] if ruletype == "ext_match_expand" else None
      # try the matcher. If true, return an expansion object
      expansion = self._try_get_expansion_if_match_on_slot(slot, rule_id, ruletype, match, expand, flag_dict, {"choose_idx": choose_idx})
      if expansion is not None:
        if TRANS_VERBOSE > 0: print("# _possible_expansion_iter_gen matched!", slot, expansion)
        yield expansion
        choose_idx += 1
    return None
  
  def _get_expansion_for_slot(self, slot_id, idx):
    slot = self._slot_dict[slot_id]
    if slot_id not in self.__slot_expand_info_dict:
      self.__slot_expand_info_dict[slot_id] = [[], False, self._possible_expansion_iter_gen(slot)]
    expan_list, is_done, iterobj = self.__slot_expand_info_dict[slot_id]
    if idx < len(expan_list): 
      return expan_list[idx]
    else:
      if is_done: return None
      try:
        while len(expan_list) < idx + 3: # use +2
          nextstuff = next(iterobj)
          assert nextstuff is not None
          expan_list.append(nextstuff)    
      except StopIteration: 
        self.__slot_expand_info_dict[slot_id][1] = True
        self.__slot_expand_info_dict[slot_id][2] = None
      if idx < len(expan_list): return expan_list[idx]
      else: return None
    
  def _get_expansions_stat_for_slot(self, slot_id):
    assert slot_id in self.__slot_expand_info_dict
    expan_list, is_done, _ = self.__slot_expand_info_dict[slot_id]
    return {"count":len(expan_list), "done":is_done}

  def _set_program_str(self, code_str):
    # parse the code, set self.expansion_programs
    print(f"\n\n++++++++++++++++++++++++++++++++++++++++ _set_program_str. {len(code_str)} ++++++++++++++++++++++++++++++++++++++++\n")
    expansion_programs, dbg_info = grammar_rules.parse_analyze_rules(code_str)
    self.expansion_programs = expansion_programs
    self.program_dbg_info["expansion_programs"] = dbg_info
    print("++++++++++++  set self.expansion_programs")

  @classmethod
  def _pretty_range_cursor(cls, range_cursor):
    additional_info = []
    for idx in range(range_cursor[1], range_cursor[2]):
      cursor_elem = range_cursor[0][idx]
      if isinstance(cursor_elem, list) and len(cursor_elem) > 0:
        additional_info.append(str(cursor_elem[0]))
      elif isinstance(cursor_elem, str):
        additional_info.append("str:" + cursor_elem)
      elif isinstance(cursor_elem, int):
        additional_info.append("int:" + str(cursor_elem))
      else:
        print("# ERROR!", cursor_elem)
        assert False
    return f"(len={str(len(range_cursor[0]))} start={range_cursor[1]} end={range_cursor[2]} {additional_info}))"


  def is_anno_compatible(self, matcher_anno, intree_anno):
    # print("matcher_anno:", matcher_anno, file=sys.stderr)
    # print("intree_anno:", intree_anno, file=sys.stderr)
    # return True
    # FUTURE TODO: improve performance
    matcher_anno_dict = {x[0]:x[1] for x in matcher_anno[1:]}
    intree_anno_dict = {x[0]:x[1] for x in intree_anno[1:]}
    for key in matcher_anno_dict:
      if key not in intree_anno_dict: return False
      if matcher_anno_dict[key] != intree_anno_dict[key]: return False
    return True
  
  # if successful, this function should return an expand object
  def _try_get_expansion_if_match_on_slot(self, slot, rule_id, m_ruletype, m_match, m_expand, m_flag_dict, notes):
    # print("_try_get_expansion_if_match_on_slot:", slot, m_match, m_expand)
    # the range cursor is a cursor on a list of source nodes
    is_ext_ruletype = m_ruletype == "ext_match_expand"
    m_matcher = None
    m_range_cursor = slot.range_cursor
    if m_match[0] == "fragment": 
      m_matcher = m_match[1:]
      # TODO: check if there's bug
    else:
      m_matcher = [m_match]

    matching_ids = []
    slot_cursors = []
    matching_values = []
    matching_strs = []
    matching_liststrs = []
    matching_anynts = []
    matching_annos = []
    
    # change range cursor to be a tuple (ast_node, start_idx, end_idx) end_idx is the length if cursor is all.
    def _try_match_rec(range_cursor, range_cursor_idx: cython.int, matcher, matcher_idx: cython.int) -> cython.bint:
      # assert range_cursor[2] <= len(range_cursor[0])
      if range_cursor_idx >= range_cursor[2] and matcher_idx >= len(matcher):
        return True
      if matcher_idx < len(matcher): 
        assert len(matcher) > 0
        current_matcher_elem = matcher[matcher_idx]
        if current_matcher_elem == '"*"':
          # all the rest is a cursor
          slot_cursors.append((range_cursor[0], range_cursor_idx, range_cursor[2]))
          # nothing to update for matching ids
          return True
        elif current_matcher_elem == '"."':
          # everything until the next NT is a cursor
          # everything after the next NT would be the rest to match
          split_idx = None
          visit_cur_idx : cython.int
          for visit_cur_idx in range(range_cursor_idx, range_cursor[2]):
            visit_elem = range_cursor[0][visit_cur_idx]
            if _is_elem_NT(visit_elem):
              split_idx = visit_cur_idx + 1
              break
          if split_idx is None: return False   # NT not found
          else:
            # NT found, cursor endswith NT
            slot_cursors.append((range_cursor[0], range_cursor_idx, split_idx))
            return _try_match_rec(range_cursor, split_idx, matcher, matcher_idx + 1)
        elif current_matcher_elem == '"_val_"':
          assert len(matcher) == 1
          is_invalid = len(range_cursor[0]) != 3 or (range_cursor[2] - range_cursor[1]) != 1 or range_cursor_idx != 2
          if is_invalid:  
            print("# UNEXPECTED range_cursor for _val_ match: ", range_cursor, range_cursor_idx)
            assert "UNEXPECTED range_cursor" == 0
          matching_values.append(range_cursor[0][2])
          return True
        elif current_matcher_elem == '"_str_"':
          if range_cursor_idx >= range_cursor[2]: return False # TOCHECK: out of length is failed to match.
          current_range_elem = range_cursor[0][range_cursor_idx]
          if not isinstance(current_range_elem, str): return False
          matching_strs.append(current_range_elem)
          return _try_match_rec(range_cursor, range_cursor_idx + 1, matcher, matcher_idx + 1)
        elif current_matcher_elem == '"_liststr_"':
          assert is_ext_ruletype
          temp_rgcursor_idx : cython.int = range_cursor_idx
          temp_liststr = []
          while True:
            if temp_rgcursor_idx >= range_cursor[2]: break
            current_range_elem = range_cursor[0][temp_rgcursor_idx]
            if isinstance(current_range_elem, str): 
              temp_liststr.append(current_range_elem)
              temp_rgcursor_idx += 1
            else: break
          matching_liststrs.append(temp_liststr)
          return _try_match_rec(range_cursor, temp_rgcursor_idx, matcher, matcher_idx + 1)
        elif current_matcher_elem == '"_anno_"':
          current_range_elem = range_cursor[0][range_cursor_idx]
          if not isinstance(current_range_elem, list): raise UnderstoodException("_anno_ meet none-annotation element: Not a list.")
          if current_range_elem[0] != "anno":  raise UnderstoodException("_anno_ meet none-annotation element: elem head: " + current_range_elem[0])
          matching_annos.append(current_range_elem)
          return _try_match_rec(range_cursor, range_cursor_idx + 1, matcher, matcher_idx + 1)
        else:
          # not direct string, must be a list
          assert isinstance(current_matcher_elem, list)
          matcher_operator = current_matcher_elem[0]

          if range_cursor_idx >= range_cursor[2]:
            if matcher_operator == "val" or matcher_operator == "str" or matcher_operator.startswith('"'):
              return False
            elif matcher_operator == "nostr":
              return _try_match_rec(range_cursor, range_cursor_idx, matcher, matcher_idx + 1)
            else:
              print("UNEXPECTED range_cursor_idx out of length (range):", range_cursor_idx, range_cursor, file=sys.stderr)
              print("UNEXPECTED range_cursor_idx out of length (matcher):", matcher_idx, matcher, file=sys.stderr)
              assert "UNEXPECTED range_cursor_idx out of length" == 0
          else:
            if matcher_operator == "val":
              assert len(current_matcher_elem) == 2
              match_val = current_matcher_elem[1]
              is_invalid = len(range_cursor[0]) != 3 or (range_cursor[2] - range_cursor[1]) != 1 or range_cursor_idx != 2
              if is_invalid:  
                print("# UNEXPECTED range_cursor for val match: ", range_cursor, range_cursor_idx)
                assert "UNEXPECTED range_cursor for val match" == 0
              range_val = range_cursor[0][range_cursor_idx]
              if not isinstance(range_val, str) and not isinstance(range_val, int) and not isinstance(range_val, float): return False
              if str(range_val) == str(match_val): return True  # TODO: FUTURE OPTIMIZE
              return False
            elif matcher_operator == 'str':
              assert len(current_matcher_elem) == 2
              match_val = current_matcher_elem[1]   
              should_be_str_val = range_cursor[0][range_cursor_idx]
              if not isinstance(should_be_str_val, str): return False
              if str(should_be_str_val) != str(match_val): return False # TODO: Future optimize
              return _try_match_rec(range_cursor, range_cursor_idx + 1, matcher, matcher_idx + 1)
            elif matcher_operator == "nostr":
              assert len(current_matcher_elem) == 1
              should_not_be_str_val = range_cursor[0][range_cursor_idx]
              if isinstance(should_not_be_str_val, str): return False
              return _try_match_rec(range_cursor, range_cursor_idx, matcher, matcher_idx + 1)
            elif matcher_operator == "anno":
              should_be_anno = range_cursor[0][range_cursor_idx]
              if not isinstance(should_be_anno, list): raise UnderstoodException("(anno ...) meet none-annotation element: Not a list.")
              if should_be_anno[0] != "anno":  raise UnderstoodException("(anno ...) meet none-annotation element: elem head: " + should_be_anno[0])
              if not self.is_anno_compatible(current_matcher_elem, should_be_anno): return False
              return _try_match_rec(range_cursor, range_cursor_idx + 1, matcher, matcher_idx + 1)
            else:
              # not special operators, must be grammar NT constructs
              if not matcher_operator.startswith('"'):
                print("# Unknown operator in _try_match_rec. expecting NT constructs:", matcher_operator, file=sys.stderr)
                assert False
              current_matcher_type = matcher_operator[1:-1] # TODO: future optimize
              assert current_matcher_type != "fragment" and current_matcher_type != "anno"

              for visit_cur_idx in range(range_cursor_idx, range_cursor[2]):
                visit_elem = range_cursor[0][visit_cur_idx]
                if isinstance(visit_elem, str):
                  # this is not an NT. It is a T. We are currently matching against an NT.
                  # print("# Skipping T:", visit_elem)
                  continue 
                if visit_elem[0] == "anno":
                  #  we are currently matching against NT. anno if not caputured in earlier cases, in this case it will be skipped.
                  continue
                else:
                  assert _is_elem_NT(visit_elem)
                  visit_type = _get_elem_NT_type(visit_elem)
                  is_direct_match = visit_type == current_matcher_type
                  is_arbitrarynt_match = current_matcher_type == "_anynt_"
                  
                  if is_direct_match or (is_arbitrarynt_match and is_ext_ruletype):
                    if is_direct_match:
                      if TRANS_VERBOSE > 0: print("_try_match_rec MATCHED! nice.", visit_type)
                    if is_arbitrarynt_match:
                      if is_ext_ruletype:
                        if TRANS_VERBOSE > 0: print("_try_match_rec ARBITRARY MATCHED! nice.", visit_type)
                        matching_anynts.append(f'"{visit_type}"')
                      else:
                        assert "ONLY_EXT_RULES_SUPPORT_ARBITRARY_MATCH" == 0 
                    # type match. add matching id.
                    matching_ids.append(visit_elem[1])
                    # check if the matching element is matched
                    children_matcher = current_matcher_elem[1:] # TODO: optimize
                    is_elem_matching = _try_match_rec((visit_elem, 2, len(visit_elem)), 2, children_matcher, 0)
                    if not is_elem_matching: return False
                    return _try_match_rec(range_cursor, visit_cur_idx + 1, matcher, matcher_idx + 1)
                  else:
                    if TRANS_VERBOSE > 0: print("_try_match_rec mismatch:", visit_type, current_matcher_type)
                    # mismatch!
                    return False
              # no match or mismatch
              return False
      else:
        # matcher element is empty
        # the rest of the cursor must all be terminals
        for visit_cur_idx in range(range_cursor_idx, range_cursor[2]):
          visit_elem = range_cursor[0][visit_cur_idx]
          if isinstance(visit_elem, str):
            continue 
          else:
            # contains non terminal
            return False
        # loop done. All of them are terminals.
        return True

    # try match rec
    is_matched = _try_match_rec(m_range_cursor, m_range_cursor[1], m_matcher, 0)
    if TRANS_VERBOSE > -10 and is_matched: 
        print("# _try_match_on_range_cursor MATCH: ", "   cursor: ", 
          TransSession._pretty_range_cursor(m_range_cursor), 
          "   matcher: ", m_matcher, file=sys.stderr)
    # print("_try_match_on_range_cursor:", is_matched)
    if not is_matched: return None
    new_notes = copy.copy(notes)
    new_notes["rule_id"] = rule_id
    return self._create_expansion(
      slot.slot_id, m_expand, matching_ids, slot_cursors, 
      matching_values, matching_strs, matching_anynts, matching_liststrs,
      matching_annos,
      new_notes) # notes (for human debugging) not implemented


  # relation:
  #  each slot belongs to an expansion
  #  a fixed list of slots belong to the same expansion
  #  each expansion belong to one slot
  #  multiple expansions can be alternatives of the same slot
  def get_translation(self, choices, auto_backward=True):
    choice_type = choices["type"]
    if choice_type == "STEP":
      choices_dict = {x:y for x,y in choices["choices_list"]}
    elif choice_type == "ASTNODE":
      choices_dict = {tuple(x):y for x,y in choices["choices_list"]}
    
    allowed_backward_alt_step = 0
    def _get_or_create_next_alt_func(alt_node):
      if TRANS_VERBOSE > -10: print("# _get_or_create_next_alt_func. current_alt_node:", alt_node)
      assert len(alt_node["todo_slot_ids"]) > 0

      slot_expan_idx = 0
      new_step = alt_node["alt_step"] + 1
      if choice_type == "STEP":
        if new_step in choices_dict: slot_expan_idx = choices_dict[new_step]
      elif choice_type == "ASTNODE":
        todo_slot_id = alt_node["todo_slot_ids"][0]
        todo_slot = self._slot_dict[todo_slot_id]
        ast_node, start_idx, end_idx = todo_slot.range_cursor
        if new_step == 1:
          assert len(ast_node) == 1
        else:
          # if (len(ast_node) < 2):
          #   print("Unexpected ast_node: ", ast_node, file=sys.stderr)
          #   assert "unexpected ast_node length." == 0
          ast_id = ast_node[1]
          if not isinstance(ast_id, int):
            print("Unexpected ast_id: ", ast_id, file=sys.stderr)
            assert "unexpected ast_id" == 0
          key = (ast_id, start_idx, end_idx)
          if key in choices_dict:
            slot_expan_idx = choices_dict[key]
      else:
        assert "Unknown choice_type" == 0

      next_alt_node = self._get_or_create_alt_node(alt_node, slot_expan_idx)
      return next_alt_node
    
    def _get_nth_parent(alt_node, n):
      if alt_node is None: return None
      if n == 0: return alt_node
      return _get_nth_parent(self._alt_tree_dict[alt_node["prev_alt_id"]], n - 1)

    def _backward_alt_next_choice_func(alt_node, child_choose_idx):
      nonlocal allowed_backward_alt_step
      if auto_backward == False:
        raise NormalException("Rejection occurred and automatic backwarding is disabled.")
      allowed_backward_alt_step = max(allowed_backward_alt_step, alt_node["alt_step"] - self._BACKWARD_MAX_STEP)
      if alt_node["alt_step"] < allowed_backward_alt_step:
        raise NormalException("Automatic backwarding failed to find alternative choices. (back limit)")
      next_choices_status = alt_node["next_choices_status"]
      if child_choose_idx + 1 >= next_choices_status["count"] and next_choices_status["done"]:
        prev_alt_id = alt_node["prev_alt_id"]
        if prev_alt_id is None:
          raise NormalException("Automatic backwarding failed to find alternative choices. (back to root)")
        return _backward_alt_next_choice_func(self._alt_tree_dict[prev_alt_id], alt_node["choose_idx"])
      else: 
        new_ch_idx = child_choose_idx + 1
        if choice_type == "STEP":
          next_step = alt_node["alt_step"] + 1
          if TRANS_VERBOSE > -11: print(f"++++++ _backward_alt_func set to: (alt_id:{alt_node['alt_id']}) (next_step:{next_step}) (new_ch_idx:{new_ch_idx})")
          return alt_node, next_step, new_ch_idx
        elif choice_type == "ASTNODE":
          slot_id = alt_node["todo_slot_ids"][0]
          slot_range_cursor = self._slot_dict[slot_id].range_cursor
          next_range_key = (slot_range_cursor[0][1], slot_range_cursor[1], slot_range_cursor[2])
          if TRANS_VERBOSE > -11: print(f"++++++ _backward_alt_func set to: (alt_id:{alt_node['alt_id']}) (next_range_key:{next_range_key}) (new_ch_idx:{new_ch_idx})")
          return alt_node, next_range_key, new_ch_idx
        else:
          assert "Unsupported choice_type" == 0
    
    error_point_dbg_info = None
    def _get_alt_parser_result(alt_node):
      try:
        parser_result = self._encure_parser_result(alt_node)
        if TRANS_VERBOSE > -10: 
          print("# _get_or_create_next_alt_func PARSE is_acceptable:", parser_result["is_acceptable"],
            " is_done:", parser_result["is_done"])
        return parser_result["is_acceptable"], parser_result["stuck_slot_id"], parser_result["is_done"]
      except Exception as err:
        error_alt_parser_result = self._alt_parser_result_dict[alt_node["alt_id"]]
        assert error_alt_parser_result["is_error"]
        error_point_dbg_info = error_alt_parser_result["dbg_info"]
        raise err

    current_alt_node = self._alt_tree_dict[0]
    is_expand_loop_successful = False
    error_info = {"msg": None}
    time1 = timeit.default_timer()
    try:
      print(">>>>> _expand_loop <<<<<")
      MAX_LOOPCOUNT = 15000
      loop_count = 0
      last_checkpoint_step = 0
      while True:
        loop_count += 1
        if loop_count > MAX_LOOPCOUNT: 
          print("# _expand_loop MAX_LOOP exceeded.")
          assert 0 == "MAX_LOOP_excedded"
        if TRANS_VERBOSE > -10: print(f"############## _expand_loop {loop_count} ... ")
        assert len(current_alt_node["todo_slot_ids"]) > 0
        next_alt_node = _get_or_create_next_alt_func(current_alt_node)
        if next_alt_node is None:
          if TRANS_VERBOSE > -11: print("#!!!!!!!!!! No expansion for todo slot. Backward...\n\n")
          assert "How_to_deal_with_this_case" == 0
          # current_alt_node, next_alt_step, next_choose_idx = _backward_alt_next_choice_func(current_alt_node)
          # choices_dict[next_alt_step] = next_choose_idx
          # continue
        else:
          par_alt_node = current_alt_node
          current_alt_node = next_alt_node
          is_acceptable, stucking_slot_id, is_done = _get_alt_parser_result(current_alt_node)
          if not is_acceptable:
            expansion = current_alt_node["expansion"]
            if TRANS_VERBOSE > -11: print(f"!!!!!!!!!! _expand_loop apply_expand_func FAILED on exid:{expansion.ex_id}" + 
                  f" (corres_slot_id:{expansion.corres_slot_id}). Backward...\n\n")
            # optimization begin
            if par_alt_node["alt_step"] - last_checkpoint_step > self._BACKWARD_MAX_STEP:
              nth_parent = _get_nth_parent(par_alt_node, self._BACKWARD_MAX_STEP)
              if nth_parent is not None: 
                self._update_alt_node_as_checkpoint(nth_parent["alt_id"])
                last_checkpoint_step = nth_parent["alt_step"]
            # optimization end
            current_alt_node, update_key, update_choose_idx = _backward_alt_next_choice_func(par_alt_node, current_alt_node["choose_idx"])
            choices_dict[update_key] = update_choose_idx
            continue
          elif len(current_alt_node["todo_slot_ids"]) == 0:
            assert is_done
            break
          else:
            # optimization begin
            if par_alt_node["alt_step"] - last_checkpoint_step > self._SNAPSHOT_INTERVAL:
              self._update_alt_node_as_checkpoint(par_alt_node["alt_id"])
              last_checkpoint_step = par_alt_node["alt_step"]
            # optimization end
            expansion = current_alt_node["expansion"]
            if TRANS_VERBOSE > -11: print(f"************** _expand_loop {loop_count} apply_expand_func SUCCEED on exid:{expansion.ex_id} (corres_slot_id:{expansion.corres_slot_id})\n\n")
            continue
      is_expand_loop_successful = True
      print("# _expand_loop FINISHED SUCCESSFULLY.")

    except Exception as err:
      print("############## traceback ##############", file=sys.stderr)
      traceback.print_exc()
      print("############## err ##############", file=sys.stderr)
      print(type(err))
      print(err)
      if isinstance(err, AssertionError):
        consts.HIT_UNEXPECTED_ERROR = True
        error_msg = "[FATAL_ERROR] SERVER STATE MIGHT BE CORRUPTED. Please check the log. " + str(err)
        consts.HIT_UNEXPECTED_ERROR_MESSAGE = error_msg
        error_info["msg"] = error_msg
      elif isinstance(err, NormalException):
        error_info["msg"] = "[NormalException] " + str(err)
      elif isinstance(err, UnderstoodException):
        error_info["msg"] = "[UnderstoodException] " + str(err)
      else:
        error_info["msg"] = "[UNEXPECTED_ERROR] " + str(type(err)) + " " + str(err)
    time2 = timeit.default_timer()
    print("\n# ----- time elapsed:", time2 - time1)
    if is_expand_loop_successful:
      tar_ast = self._get_alt_partial_ast(current_alt_node)
      return True, tar_ast, choices_dict, None, self._get_alt_debug_history(current_alt_node)
    else: return False, None, choices_dict, error_info, self._get_alt_debug_history(current_alt_node) # TODO: error

  def get_session_dbg_info(self):
    return {
      "program": self.program_dbg_info
    }
  


############################# utils #############################
@cython.cfunc
@cython.inline
def _is_elem_NT(visit_elem) -> cython.bint:
  if not isinstance(visit_elem, list): return False
  if visit_elem[0] == "anno": return False
  assert visit_elem[0] != "fragment"
  assert isinstance(visit_elem[1], int)
  return True

@cython.cfunc
@cython.inline
def _get_elem_NT_type(visit_elem):
  return visit_elem[0]
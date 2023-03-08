import json
import consts
from tree_sitter import Parser

def _anno_func_py_string(ann, context):
  startpos = ann[0]
  endpos = ann[1]
  subs = context[startpos:endpos]
  stype = ""
  if subs.startswith("f"): stype = "f"
  elif subs.startswith("r"): stype = "r"
  elif subs.startswith("b"): stype = "b"
  else: 
    if not (subs.startswith('"') or subs.startswith("'")):
      print("_anno_func_py_string UNEXPECTED:", subs)
      assert "parse_error" == 0 or (subs.startswith('"') or subs.startswith("'"))
  quote = None
  if subs.endswith('\"\"\"'): quote = '\"\"\"'
  elif subs.endswith("\'\'\'"): quote = "\'\'\'"
  elif subs.endswith('\"'): quote = '\"'
  elif subs.endswith("\'"): quote = "\'"
  else: assert 0 == "py.string does not endswith ' or \""
  return ["anno", ['"stype"', f'"{stype}"'], ['"quote"', f'{json.dumps(quote)}']]

_anno_func_dict = {
  "py.string": _anno_func_py_string
}

parsers_dict = {}
def parse_text_dbg(language, text, type_prefix):
  if language not in parsers_dict:
    parsers_dict[language] = Parser()
    parsers_dict[language].set_language(language)
  parser = parsers_dict[language]
  tree = parser.parse(bytes(text, "utf8"))

  root_node = tree.root_node
  if consts.DEBUG_VERBOSE > 0: print(root_node.sexp())

  print(f"\n---------- parse_text_dbg ({type_prefix}, length: {len(text)}) -----------")

  def traverse(tree, fn_before, fn_visit, fn_before_child, fn_after):
    def _traverse(node):
      fn_before(node)
      fn_visit(node)
      for child in node.children:
        fn_before_child(child)
        _traverse(child)
      fn_after(node)
    # calling _traverse
    _traverse(tree.root_node)
    

  current_node_idx = 0
  ann_info = {}
  
  extra_root = []
  ast_scope_stack = [extra_root]
  def fn_before(node):
    if node.is_named == False: return
    if consts.DEBUG_VERBOSE > 0: print("(", end="")
  def fn_visit(node):
    def add_id():
      nonlocal current_node_idx
      if consts.DEBUG_VERBOSE > 0: print(f" {current_node_idx}", end="")
      ann_info[current_node_idx] = [node.start_byte, node.end_byte, node.start_point, node.end_point]
      current_node_idx += 1
      return current_node_idx - 1
    
    if node.is_named:      
      sub_ast_list = []
      ast_scope_stack[-1].append(sub_ast_list)
      ast_scope_stack.append(sub_ast_list)

      elem = type_prefix + "." + node.type
      if consts.DEBUG_VERBOSE > 0: print(elem, end="")
      sub_ast_list.append(elem)

      new_id = add_id()
      sub_ast_list.append(new_id)

      if elem in _anno_func_dict:
        anno_func = _anno_func_dict[elem]
        anno = anno_func(ann_info[new_id], text)
        if anno is not None:
          sub_ast_list.append(anno)

      if len(node.children) == 0:
        # named (typed), but no children. Should be an external symbol
        elem = json.dumps(text[node.start_byte:node.end_byte])
        if consts.DEBUG_VERBOSE > 0: print("", elem, end="")
        sub_ast_list.append(elem)
    else:
      # not named
      # print(type_prefix + ".a", end="")
      # add_id()
      elem = json.dumps(node.type)
      if consts.DEBUG_VERBOSE > 0: print(elem, end="")
      ast_scope_stack[-1].append(elem)
      
    
  def fn_after(node):
    if node.is_named == False: return
    ast_scope_stack.pop()
    if consts.DEBUG_VERBOSE > 0: print(")", end="")
  def fn_before_child(child):
    if consts.DEBUG_VERBOSE > 0: print(" ", end="")

  traverse(tree, fn_before, fn_visit, fn_before_child, fn_after)
  assert len(ast_scope_stack) == 1
  assert len(extra_root) == 1
  # print("\n-------------------------")
  # print(json.dumps(extra_root[0]))
  return extra_root[0], ann_info
  # print(ann_info)



# old code using cursor ---------------------
# from tree_sitter import Tree, TreeCursor
# def traverse_tree_cursor_gen(tree: Tree):
#   cursor = tree.walk()
#   reached_root = False
#   while reached_root == False:
#     print(cursor.node.type, end="")
#     yield cursor.node
#     if cursor.goto_first_child():
#       print("{", end="")
#       continue
#     if cursor.goto_next_sibling():
#       print(",", end="")
#       continue
#     retracing = True
#     while retracing:
#       if not cursor.goto_parent():
#         retracing = False
#         reached_root = True
#       else:
#         print("}", end="")
#       if cursor.goto_next_sibling():
#         print(",", end="")
#         retracing = False
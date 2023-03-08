import sys
import os
INTERPRET_MODE = False
print(f"=============== DuoGlotCore Start in {'INTERPRETED' if INTERPRET_MODE else 'COMPILED'} mode ===============", file=sys.stderr)

if INTERPRET_MODE: os.system("rm -rf ./*cpython-*.so")
else: os.system("python3 ./setup_build.py build_ext --inplace")

# don't use pyximport due to lack of control and annotation
# import pyximport; pyximport.install(language_level = "3")
import json
import flask
from flask import request, jsonify
from flask_cors import CORS
import sys
import timeit
# sys.setrecursionlimit(3000)
from tree_sitter import Language
import grammar
import ast_parse
import ast_pretty
import ast_match
import grammar_expand
import grammar_rules
import code_beautify
import util_hash

# for profiling
import cProfile, pstats, io
from pstats import SortKey

from consts import PROFILING_TYPE, PROFILING_OUTPUT_STYLE, ENABLE_CYTHON_PROFILE

if PROFILING_TYPE == "vmprof":
  try:
    import vmprof
  except:
    print("WARNING: Failed to import vmprof. Setting PROFILING_TYPE to None.")
  PROFILING_TYPE = None

if PROFILING_TYPE is not None:
  print("PROFILING tool: " + PROFILING_TYPE, file=sys.stderr)
  print("PROFILING cython: " + str(ENABLE_CYTHON_PROFILE), file=sys.stderr)
  print("PROFILING output: " + PROFILING_OUTPUT_STYLE, file=sys.stderr)

# ------------- webui initialization code -------------
print("=============== DuoGlotCore Initialization BEGIN ===============", file=sys.stderr)


app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True   # True (set to false will auto minify json response)
# app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False # already False.
app.config['MAX_CONTENT_LENGTH'] = 67108864

def read_text(fname):
  with open(fname, 'r') as f:
    return f.read()

def read_json(fname):
  with open(fname, 'r') as f:
    return json.load(f)

def save_text(filepath, content):
  print("# save to:", filepath)
  with open(filepath, 'w') as f:
    f.write(content)

language_paths = [
  './tree-sitter-util/tree-sitter-javascript',
  './tree-sitter-util/tree-sitter-python',
  # './tree-sitter-util/tree-sitter-cpp',
  # './tree-sitter-util/tree-sitter-c-sharp',
  # './tree-sitter-util/tree-sitter-java'
]

Language.build_library(
  'build/my-languages.so',
  language_paths
)

PY_LANGUAGE = Language('build/my-languages.so', 'python')
JS_LANGUAGE = Language('build/my-languages.so', 'javascript')
# CPP_LANGUAGE = Language('build/my-languages.so', 'cpp')
# CS_LANGUAGE = Language('build/my-languages.so', 'c_sharp')
# JAVA_LANGUAGE = Language('build/my-languages.so', 'java')

PY_GRAMMAR = read_json(language_paths[1] + "/src/grammar.json")
JS_GRAMMAR = read_json(language_paths[0] + "/src/grammar.json")
# CPP_GRAMMAR = read_json(language_paths[2] + "/src/grammar.json")
# CS_GRAMMAR = read_json(language_paths[3] + "/src/grammar.json")
# JAVA_GRAMMAR = read_json(language_paths[4] + "/src/grammar.json")

grammar.grm_preprocess("py", PY_GRAMMAR)
grammar.grm_preprocess("js", JS_GRAMMAR)
# grammar.grm_preprocess("cpp", CPP_GRAMMAR)
# grammar.grm_preprocess("cs", CS_GRAMMAR)
# grammar.grm_preprocess("java", JAVA_GRAMMAR)

py_not_inlined_NTs = grammar.grm_get_all_not_inlined_NTs(PY_GRAMMAR)
js_not_inlined_NTs = grammar.grm_get_all_not_inlined_NTs(JS_GRAMMAR)
# cpp_not_inlined_NTs = grammar.grm_get_all_not_inlined_NTs(CPP_GRAMMAR)
# cs_not_inlined_NTs = grammar.grm_get_all_not_inlined_NTs(CS_GRAMMAR)
# java_not_inlined_NTs = grammar.grm_get_all_not_inlined_NTs(JAVA_GRAMMAR)

GRAMMAR_DICT = {"py": PY_GRAMMAR, "js": JS_GRAMMAR} #, "java": JAVA_GRAMMAR, "cs": CS_GRAMMAR, "cpp": CPP_GRAMMAR}
NT_DICT =  {"py": py_not_inlined_NTs, "js": js_not_inlined_NTs} #, "java": java_not_inlined_NTs, "cs": cs_not_inlined_NTs, "cpp": cpp_not_inlined_NTs}

print("=============== DuoGlotCore Initialization END ===============", file=sys.stderr)

@app.route("/nts")
def get_nts():
  return jsonify({
    "py_not_inlined_NTs": py_not_inlined_NTs,
    "js_not_inlined_NTs": js_not_inlined_NTs,
    # "cpp_not_inlined_NTs": cpp_not_inlined_NTs,
    # "java_not_inlined_NTs": java_not_inlined_NTs,
    # "cs_not_inlined_NTs": cs_not_inlined_NTs
  })


def parse_core(lang, text):
  if lang == "py":
    result_ast, result_ann = ast_parse.parse_text_dbg(PY_LANGUAGE, text, "py")
  elif lang == "js":
    result_ast, result_ann = ast_parse.parse_text_dbg(JS_LANGUAGE, text, "js")
  # elif lang == "cpp":
  #   result_ast, result_ann = ast_parse.parse_text_dbg(CPP_LANGUAGE, text, "cpp")
  # elif lang == "java":
  #   result_ast, result_ann = ast_parse.parse_text_dbg(JAVA_LANGUAGE, text, "java")
  # elif lang == "cs":
  #   result_ast, result_ann = ast_parse.parse_text_dbg(CS_LANGUAGE, text, "cs")
  return result_ast, result_ann

@app.route("/parse", methods=['POST'])
def parse():
  if request.json is None:
    return jsonify({"result": None, "error_msg": "No posted data"})
  lang = request.json["language"]
  text = request.json["text"]
  result_ast, result_ann = parse_core(lang, text)
  return jsonify({"result": result_ast, "ann": result_ann})

@app.route("/matchcombo", methods=['POST'])
def matchcombo():
  if request.json is None:
    return jsonify({"result": None, "error_msg": "No posted data"})
  ast1 = request.json["ast1"]
  ast2 = request.json["ast2"]
  combo1 = request.json["combo1"]
  combo2 = request.json["combo2"]
  algo_name = request.json["algorithm"]
  match_result, typematch = ast_match.match_combo_with_AST(ast1, combo1, ast2, combo2, algo_name)
  return jsonify({"result": match_result, "typematch": typematch})


@app.route("/pairwisedist", methods=['POST'])
def pairwisedist():
  if request.json is None:
    return jsonify({"result": None, "error_msg": "No posted data"})
  trees1 = request.json["trees1"]
  trees2 = request.json["trees2"]
  algo_name = request.json["algorithm"]
  dists = []
  for i in range(len(trees2)):
    rowdist = []
    for j in range(len(trees1)):
      rowdist.append(ast_match.distance_of_AST_frags(trees2[i], trees1[j], algo_name))
    dists.append(rowdist)
  return jsonify({"result": dists})



optional_dbg_info_dict = {}
def _optional_dbg_info_save_func(obj, func):
  idobj = id(obj)
  assert idobj not in optional_dbg_info_dict
  optional_dbg_info_dict[idobj] = (obj, func)
  return idobj
def _optional_dbg_info_read_func(info_id):
  if info_id in optional_dbg_info_dict: 
    data, func = optional_dbg_info_dict[info_id]
    return func(data)
  return None

def _ast_to_code(tar_ast, tarlang):
  if tar_ast is None: return ""
  prettied_code, map_by_exid = ast_pretty.pretty_mapanno_ast(tar_ast, tarlang)
  beautified_code, mapping_list = code_beautify.beautify(tarlang, prettied_code)
  for exid in map_by_exid:
    for mapanno in map_by_exid[exid]:
      rg = mapanno["range"]
      if not (rg[1] > rg[0] and prettied_code[rg[0]:rg[1]] == mapanno["str"]):
        print("ERROR! invalid range:", mapanno, file=sys.stderr)
        assert "string mismatch or range length 0" == 0
      try:
        newrg = (mapping_list[rg[0]], mapping_list[rg[1]-1]+1)
      except Exception as e:
        print("ERROR! code map calculation failure: " + str(e), file=sys.stderr)
        print("-------- prettied code:", file=sys.stderr)
        print(prettied_code, file=sys.stderr)
        print("-------- problematic beautify and mapping:", file=sys.stderr)
        print(beautified_code, file=sys.stderr)
        print("-------- problematic range and mapping:", file=sys.stderr)
        print("rg:", rg, file=sys.stderr)
        print("mapping_list:", mapping_list, file=sys.stderr)
        assert "beautified code failed to calculate mapping" == 0
      if newrg[0] is None or newrg[1] is None:
        print("ERROR! after beautify mapping lost:", prettied_code[rg[0]:rg[1]], mapanno, file=sys.stderr)
        assert "after beautify mapping lost" == 0
      mapanno["range"] = newrg
  return beautified_code, map_by_exid


translator_cache = {}
@app.route("/translate", methods=['POST'])
def translate():
  time_before = timeit.default_timer()
  if request.json is None:
    return jsonify({"result": None, "error_msg": "No posted data"})
  src_code = request.json["source_code"]
  if not src_code.isascii():
    # CHECK: is this okay to do 
    return jsonify({"error_info":{"type": "API_PARAM_ERROR", "msg": "source_code is not ascii."}})
  srclang = request.json["source_language"]
  tarlang = request.json["target_language"]
  transprog = request.json["trans_program_str"]
  # TODO: support step_id based choices and ast_id based choices.
  choices = request.json["choices"]
  auto_backward = request.json["auto_backward"]
  slot_dedup_enabled = False
  if choices["type"] == "STEP": slot_dedup_enabled = False
  elif choices["type"] == "ASTNODE": slot_dedup_enabled = True
  else: assert "Unknown choices type" == 0
  target_grammar = GRAMMAR_DICT[tarlang]
  src_ast, src_ann = parse_core(srclang, src_code)
  translator_key = util_hash.strings_sha256([src_code, transprog, srclang, tarlang, str(slot_dedup_enabled)])

  # =============== profiler begin ===============
  if PROFILING_TYPE == "cProfile":
    pr = cProfile.Profile()
    pr.enable()
  elif PROFILING_TYPE == "vmprof":
    vmf = open("./profiles/translate.dat", "w+b")
    vmprof.enable(vmf.fileno(), period=0.00099, memory=False)
  # ---------------
  translator = None
  translator_info = None
  if translator_key in translator_cache:
    translator_info = translator_cache[translator_key]
    assert translator_info["source_code"] == src_code
    assert translator_info["trans_program_str"] == transprog
    assert translator_info["source_language"] == srclang
    assert translator_info["target_language"] == tarlang
    translator = translator_info["translator"]
  else:
    translator = grammar_expand.TransSession(
      src_code, src_ast, src_ann,
      srclang, tarlang, 
      target_grammar, transprog, 
      _optional_dbg_info_save_func, 
      slot_dedup_enabled=slot_dedup_enabled)
    translator_info = {
      "source_code": src_code, 
      "source_language": srclang, "target_language": tarlang,
      "trans_program_str": transprog, "translator": translator}
    translator_cache[translator_key] = translator_info
  assert translator is not None and translator_info is not None
  translator_dbg_info = translator.get_session_dbg_info()
  is_successful, tar_ast, choices_dict, error_info, dbg_history = translator.get_translation(choices, auto_backward) # no choices means default choices
  # TODO_FUTURE: choices_dict is excluded from resp.
  # ---------------
  if PROFILING_TYPE == "cProfile":
    pr.disable()
    s = io.StringIO()
    sortby = SortKey.CUMULATIVE
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    if PROFILING_OUTPUT_STYLE == "TEXT":
      ps.print_stats()
      print(s.getvalue())
    elif PROFILING_OUTPUT_STYLE == "FILE":
      ps.dump_stats("./profiles/translate.prof")
    else: assert False
  elif PROFILING_TYPE == "vmprof":
    vmprof.disable()
    vmf.close()

  parse_data = {"src_ast": src_ast, "src_ann": src_ann}
  time_after = timeit.default_timer()
  timespan = time_after - time_before
  if is_successful:
    time_before_pretty = timeit.default_timer()
    code, map_to_exid = _ast_to_code(tar_ast, tarlang)
    time_after_pretty = timeit.default_timer()
    return jsonify({"parse": parse_data, "timespan": timespan, "timespan_p": time_after_pretty - time_before_pretty, "result": {"ast": tar_ast, "code": code, "map_to_exid": map_to_exid}, "dbg_history": dbg_history, "translator_dbg_info": translator_dbg_info})
  else:
    print("Response error_info:", error_info)
    return jsonify({"parse": parse_data, "timespan": timespan, "timespan_p": None, "error_info": error_info, "dbg_history": dbg_history, "translator_dbg_info": translator_dbg_info})

parserule_cache = {}
@app.route("/parserules", methods=['POST'])
def parserules():
  if request.json is None:
    return jsonify({"result": None, "error_msg": "No posted data"})
  transprog = request.json["trans_program_str"]
  parserule_key = util_hash.strings_sha256([transprog])

  expansion_programs, dbg_info, error_msg = None, None, None
  if parserule_key in parserule_cache:
    expansion_programs, dbg_info, error_msg = parserule_cache[parserule_key]
  else:
    try:
      expansion_programs, dbg_info = grammar_rules.parse_analyze_rules(transprog, show_disable=True)
    except Exception as e:
      error_msg = str(e)
      print("Rule parse ERROR:", e)
    parserule_cache[parserule_key] = [expansion_programs, dbg_info, error_msg]
  
  if error_msg is not None:
    return jsonify({"error_msg": error_msg})
  else:
    return jsonify({
      "expansion_programs": expansion_programs, 
      "dbg_info": dbg_info, 
    })

@app.route("/statrules", methods=['POST'])
def statrules():
  if request.json is None:
    return jsonify({"result": None, "error_msg": "No posted data"})
  transprog = request.json["trans_program_str"]
  parserule_key = util_hash.strings_sha256([transprog])

  expansion_programs, dbg_info, error_msg = None, None, None
  if parserule_key in parserule_cache:
    expansion_programs, dbg_info, error_msg = parserule_cache[parserule_key]
  else:
    try:
      expansion_programs, dbg_info = grammar_rules.parse_analyze_rules(transprog, show_disable=True)
    except Exception as e:
      error_msg = str(e)
      print("Rule parse ERROR:", e)
    parserule_cache[parserule_key] = [expansion_programs, dbg_info, error_msg]
  
  if error_msg is not None:
    return jsonify({"error_msg": error_msg})
  else:
    return jsonify({
      "stated_rules": [{"type": x["type"]} for x in expansion_programs], 
    })


@app.route("/optdbginfo/<path:info_id>")
def optdbginfo(info_id):
  dbginfo = _optional_dbg_info_read_func(int(info_id))
  return jsonify({"is_found": dbginfo is not None, "result": dbginfo})


@app.route("/elemlist2code", methods=['POST'])
def elemlist2code():
  tarlang = request.json["target_language"]
  elem_list = request.json["elem_list"]
  ast = ast_pretty.elem_list_to_mapanno_ast(elem_list)
  code, map_by_exid = _ast_to_code(ast, tarlang)
  return jsonify({  
    "result": code,
    "map_by_exid": map_by_exid
  })

import gc
@app.route("/clearmemcache")
def clearmemcache():
  translator_cache.clear()
  optional_dbg_info_dict.clear()
  parserule_cache.clear()
  gc.collect()
  gc_stats = gc.get_stats()
  garbage_len = len(gc.garbage)
  del gc.garbage[:]
  return jsonify({  
    "result": "Mem Cache Cleared",
    "gc_stats": gc_stats,
    "garbage_len": garbage_len
  })

@app.route("/updateconstsreload", methods=['POST'])
def updateconstreload():
  constdict = request.json["consts"]
  def replace_line_startswith(text, prefix, replacement):
    lines = text.split("\n")
    return "\n".join([(replacement if x.startswith(prefix) else x) for x in lines])
  const_text = read_text("./consts.py")
  for k in constdict:
    if k in ["DEBUG_VERBOSE", "PROFILING_TYPE", "PROFILING_OUTPUT_STYLE", "ENABLE_CYTHON_PROFILE"]:
      pyval = json.dumps(constdict[k]).replace("null", "None").replace("true", "True").replace("false", "False")
      const_text = replace_line_startswith(const_text, F"{k} =", f"{k} = {pyval}")
    else: return jsonify({"error_msg": "Unknown const key: " + k})
  save_text("./consts.py", const_text)
  return jsonify({"result": "OK"})
  

import argparse
parser = argparse.ArgumentParser(description='CERTainly Core Trans Server')
parser.add_argument('--host', type=str, default="0.0.0.0", help='Host to use')
parser.add_argument('--port', type=int, default=8778, help='Port to use')
parser.add_argument('--reloader', type=bool, default=False, help='Using reloader')
args = parser.parse_args()

if __name__ == '__main__':
    app.run(host=args.host, port=int(args.port), use_reloader=args.reloader)
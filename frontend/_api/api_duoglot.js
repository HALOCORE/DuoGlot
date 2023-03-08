//////// initializer begin
(function () {
  let current_url = window.document.location.href;
  if (current_url.indexOf("/frontend/") >= 0) {
    window.SERVER_DUOGLOT_PREFIX = current_url.split("/frontend/")[0] + "/backend/duoglotcore";
  } else {
    throw Error("Unexpected origin.");
  }
})();
//////// initializer end


// specific APIs
async function matchAsync(sourceComboTree, targetComboTree, algo_name) {
  let postdata = {
    "ast1": source_AST,
    "ast2": target_AST,
    "combo1": sourceComboTree,
    "combo2": targetComboTree,
    "algorithm": algo_name
  };
  let resultStr = await postAsync(SERVER_DUOGLOT_PREFIX, "/matchcombo", postdata);
  let parseResult = JSON.parse(resultStr);
  let match_result = parseResult["result"];
  let typematch = parseResult["typematch"]
  return [match_result, typematch];
}

async function computeTreeDistancesAsync(trees1, trees2, algo_name) {
  let post_data = {
    "trees1": trees1,
    "trees2": trees2,
    "algorithm": algo_name
  };
  let resultStr = await postAsync(SERVER_DUOGLOT_PREFIX, "/pairwisedist", post_data);
  let parseResult = JSON.parse(resultStr);
  let dists = parseResult["result"];
  return dists;
}



async function clearMemCacheAsync() {
  let resultStr = await getAsync(SERVER_DUOGLOT_PREFIX, "/clearmemcache");
  let clearResult = JSON.parse(resultStr);
  console.log("# clearMemCacheAsync", clearResult);
  return clearResult;
}

async function parseAsync(text, language) {
  let resultStr = await postAsync(SERVER_DUOGLOT_PREFIX, "/parse", { "text": text, "language": language });
  let parseResult = JSON.parse(resultStr);
  let ast = parseResult["result"];
  let ann = parseResult["ann"];
  return [ast, ann];
};

async function translateAsync(src_code, srclang, tarlang, transprog, choices_type, choices_list, auto_backward=true) {
  if (typeof choices_type !== "string") throw Error("Expecting choices_type to be string");
  if (!Array.isArray(choices_list)) throw Error("Expecting choices_list to be array.");
  let postdata = {
    "source_code": src_code,
    "source_language": srclang,
    "target_language": tarlang,
    "trans_program_str": transprog,
    "choices": {
      "type": choices_type,
      "choices_list": choices_list
    },
    "auto_backward": auto_backward
  };
  let resultStr = await postAsync(SERVER_DUOGLOT_PREFIX, "/translate", postdata);
  let parseResult = JSON.parse(resultStr);
  let srcparse_result = parseResult["parse"];
  let trans_result = parseResult["result"];
  let error_info = parseResult["error_info"];
  let dbg_hisory = parseResult["dbg_history"];
  let translator_dbg_info = parseResult["translator_dbg_info"];
  let timespan = parseResult["timespan"];
  let timespan_p = parseResult["timespan_p"];
  return [srcparse_result, trans_result, error_info, dbg_hisory, translator_dbg_info, timespan, timespan_p];
}

async function parseRulesAsync(transprog) {
  let postdata = {
    "trans_program_str": transprog,
  };
  let resultStr = await postAsync(SERVER_DUOGLOT_PREFIX, "/parserules", postdata);
  let parseResult = JSON.parse(resultStr);
  let {expansion_programs, dbg_info, error_msg} = parseResult;
  return [expansion_programs, dbg_info, error_msg];
}

async function statRulesAsync(transprog) {
  let postdata = {
    "trans_program_str": transprog,
  };
  let resultStr = await postAsync(SERVER_DUOGLOT_PREFIX, "/statrules", postdata);
  let parseResult = JSON.parse(resultStr);
  let {stated_rules, error_msg} = parseResult;
  return [stated_rules, error_msg];
}


async function getOptInfoAsync(info_id) {
  let opt_info = null;
  if (info_id) {
    opt_info = await getAsync(SERVER_DUOGLOT_PREFIX, "/optdbginfo/" + info_id);
    opt_info = JSON.parse(opt_info);
    if (opt_info["is_found"]) opt_info = opt_info["result"];
    else opt_info = null;
  }
  return opt_info;
}

async function elemlist2CodeAsync(target_language, elem_list) {
  console.log("Requesting elemlist2CodeAsync:", target_language, elem_list.length); //, elem_list
  let resp_str = await postAsync(SERVER_DUOGLOT_PREFIX, "/elemlist2code", {target_language: target_language, elem_list:elem_list});
  let resp = JSON.parse(resp_str);
  return resp["result"];
}

let partial_code_cache = {};
async function cachedGetPartialCodeOptAsync(target_language, info_id) {
  if(!info_id) return "DEBUG_DATA_KEY_MISSING";
  if (info_id in partial_code_cache) return partial_code_cache[info_id];
  let opt_info_obj = await getOptInfoAsync(info_id);
  if (!opt_info_obj) return "DEBUG_DATA_VALUE_MISSING";
  let code = elemlist2CodeAsync(target_language, opt_info_obj);
  partial_code_cache[info_id] = code;
  return code;
}
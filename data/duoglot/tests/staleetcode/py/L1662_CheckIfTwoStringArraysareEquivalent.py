
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["ab", "c"], ["a", "bc"]]
    # output: true
    # EXPLANATION:  word1 represents string "ab" + "c" -> "abc" word2 represents string "a" + "bc" -> "abc" The strings are the same, so return true.
    ,
    # example 2
    [["a", "cb"], ["ab", "c"]]
    # output: false
    ,
    # example 3
    [["abc", "d", "defg"], ["abcddefg"]]
    # output: true
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### arrayStringsAreEqual 
from typing import *
def f_gold(word1: List[str], word2: List[str]) -> bool:
    s1, s2 = ''.join(word1), ''.join(word2)
    return s1 == s2
"-----------------"
test()


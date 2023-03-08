
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["a", "a", "b", "b", "c", "c", "c"]]
    # output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
    # EXPLANATION:  The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
    ,
    # example 2
    [["a"]]
    # output: Return 1, and the first character of the input array should be: ["a"]
    # EXPLANATION:  The only group is "a", which remains uncompressed since it's a single character.
    ,
    # example 3
    [["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]]
    # output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
    # EXPLANATION:  The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### compress 
from typing import *
def f_gold(chars: List[str]) -> int:
    i, k, n = 0, 0, len(chars)
    while i < n:
        j = i + 1
        while j < n and chars[j] == chars[i]:
            j += 1
        chars[k] = chars[i]
        k += 1
        if j - i > 1:
            cnt = str(j - i)
            for c in cnt:
                chars[k] = c
                k += 1
        i = j
    return k
"-----------------"
test()


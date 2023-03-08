
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 1, 3, 6]]
    # output: false
    ,
    # example 2
    [[2, 1, 2, 6]]
    # output: false
    ,
    # example 3
    [[4, -2, 2, -4]]
    # output: true
    # EXPLANATION:  We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### canReorderDoubled 
from collections import Counter
from typing import *
def f_gold(arr: List[int]) -> bool:
    freq = Counter(arr)
    if freq[0] & 1:
        return False
    for x in sorted(freq, key=abs):
        if freq[x << 1] < freq[x]:
            return False
        freq[x << 1] -= freq[x]
    return True
"-----------------"
test()



# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[5, 4, 3, 2, 1], [1, 1, 2, 2, 3], 3, 1]
    # output: 9
    # EXPLANATION:  The subset chosen is the first, third, and fifth items.
    ,
    # example 2
    [[5, 4, 3, 2, 1], [1, 3, 3, 3, 2], 3, 2]
    # output: 12
    # EXPLANATION:  The subset chosen is the first, second, and third items.
    ,
    # example 3
    [[9, 8, 8, 7, 6], [0, 0, 0, 1, 1], 3, 1]
    # output: 16
    # EXPLANATION:  The subset chosen is the first and fourth items.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### largestValsFromLabels 
from collections import Counter
from typing import *
def f_gold(values: List[int], labels: List[int], numWanted: int, useLimit: int
) -> int:
    arr = list(zip(values, labels))
    arr.sort(reverse=True)
    cnt = Counter()
    ans = num = 0
    for v, l in arr:
        if cnt[l] < useLimit:
            cnt[l] += 1
            num += 1
            ans += v
        if num == numWanted:
            break
    return ans
"-----------------"
test()



# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[4, 2, 3, 0, 3, 1, 2], 5]
    # output: true
    # EXPLANATION:   All possible ways to reach at index 3 with value 0 are:  index 5 -> index 4 -> index 1 -> index 3  index 5 -> index 6 -> index 4 -> index 1 -> index 3
    ,
    # example 2
    [[4, 2, 3, 0, 3, 1, 2], 0]
    # output: true
    # EXPLANATION: One possible way to reach at index 3 with value 0 is:  index 0 -> index 4 -> index 1 -> index 3
    ,
    # example 3
    [[3, 0, 2, 1, 2], 2]
    # output: false
    # EXPLANATION: There is no way to reach at index 1 with value 0.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### canReach 
from collections import deque
from typing import *
def f_gold(arr: List[int], start: int) -> bool:
    n = len(arr)
    q = deque([start])
    while q:
        i = q.popleft()
        if arr[i] == 0:
            return True
        for j in [i + arr[i], i - arr[i]]:
            if 0 <= j < n and arr[j] >= 0:
                q.append(j)
        arr[i] = -1
    return False
"-----------------"
test()


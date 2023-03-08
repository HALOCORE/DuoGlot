from L1861_RotatingtheBox import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[["#", ".", "#"]]]
    # output: [["."],         ["#"],         ["#"]]
    ,
    # example 2
    [[["#", ".", "*", "."], ["#", "#", "*", "."]]]
    # output: [["#","."],         ["#","#"],         ["*","*"],         [".","."]]
    ,
    # example 3
    [[["#", "#", "*", ".", "*", "."], ["#", "#", "#", "*", ".", "."], ["#", "#", "#", ".", "#", "."]]]
    # output: [[".","#","#"],         [".","#","#"],         ["#","#","*"],         ["#","*","."],         ["#",".","*"],         ["#",".","."]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()

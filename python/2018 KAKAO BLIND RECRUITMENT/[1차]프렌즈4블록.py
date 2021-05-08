import numpy as np
def solution(m, n, board):
    board = np.array(board).T
    print(board)
    
    '''
    del_num = True
    answer = 0
    while del_num:
        del_num = numberOfBlock(m, n, board) # 지워지는 블록 수
        answer += del_num
        break
    '''
print(solution(6, 6, 
    ["TTTANT", 
    "RRFACC", 
    "RRRFCC", 
    "TRRRAA", 
    "TTMMMF", 
    "TMMTTJ"]
))
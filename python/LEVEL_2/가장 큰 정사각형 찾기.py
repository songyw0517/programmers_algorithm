def is_square(board, width, t, k, row, col):
    for i in range(t, t+width):
        for j in range(k-width, k):       
            if board[i][j]!=1:
                return False
    return True
    
def solution(board):
    count_one = 0
    row = len(board)
    col = len(board[0])
    for i in board:
        count_one += sum(i)
    if count_one<4:
        return 1
    i = j = width = answer=0
    while i<=row:     
        if j<col:
            if board[i][j]==1:
                width+=1
                j+=1
                count_one-=1
                continue
            else: # 0을 만나면, check
                if width:
                    if i+width<=row: # 정사각형을 만족할 수 있는지 확인
                        if is_square(board, width, i, j, row, col):
                            if answer<width*width:
                                answer = width*width
                    width=0
                j+=1
        else: # j>col
            if width:
                if i+width<=row:
                    if is_square(board, width, i, j, row, col):
                        if answer<width*width:
                            answer = width*width
                    width=0
            j=0
            i+=1
    return answer
print(
    solution([
        [1,1,0,0,1,1,1,1],
        [1,1,1,0,1,1,1,1],
        [1,1,1,1,1,1,1,1], 
        [0,0,1,0,1,1,1,1]
    ])
)
'''
[0,1,1,1], 3
[1,1,1,1], 4
[1,1,1,1], 4
[0,0,1,0]  1
-> 9

[1,1,1,0], 3
[1,1,1,1], 4
[1,1,1,1], 4
[1,0,1,1]  3
-> 9

[0,1,1,0],
[1,1,1,0],
[1,1,1,1],
[0,0,1,0]
-> 4

[0,1,0,0],
[1,1,1,0],
[1,1,1,1],
[0,0,1,0]
-> 4

[1,1,0,0,1,1,1,1], -> 0 1 4 5 6 7
[1,1,1,0,1,1,1,1], -> 0 1 2 4 5 6 7
[1,1,1,1,1,1,1,1], -> 0 1 2 4 5 6 7 
[0,0,1,0,1,1,1,1]  -> 2 4 5 6 7
->16


'''
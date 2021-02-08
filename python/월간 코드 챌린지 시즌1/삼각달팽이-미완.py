def solution(n):
    answer = []
    number = 1
    last_number = 0
    temp = n
    while temp>=0:
        last_number+=temp
        temp-=1
    dir = 1 # 아래

print(solution(4))
def solution(numbers):
    answer = [[],[],[],[],[],[],[],[],[]]
    for i in range(1, 10):
        for n in numbers:
            answer[int(str(n)[0])].append(n)
        for i in answer:
            if i!=[]:
                i.sort()
        answer.pop([])
        break
    

    print(answer)
print(solution([2,3,1,222,22,13,12]))


'''
2 3 1 222 22 13 12 -> 1 13 / 2 22 222 / 3

시간 초과

from itertools import permutations
def solution(numbers):
    answer = permutations(numbers)
    result = []
    for i in answer:
        result.append(int(''.join(map(str, list(i)))))
    
    return str(max(result))
print(solution([6,10,2]))
'''
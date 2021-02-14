def solution(numbers):
    for i, value in enumerate(numbers):
        for j in range(10,0,-1):
            
            print(j)
print(solution([1,2,3,4,5]))

'''
from itertools import permutations
def solution(numbers):
    answer = permutations(numbers)
    
    result = []
    for i in answer:
        result.append(int(''.join(map(str, list(i)))))
    
    #return str(max(result))
print(solution([6,10,2]))
'''
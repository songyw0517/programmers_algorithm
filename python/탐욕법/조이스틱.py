def solution(name):
    answer = 0
    index = 0
    AList = []
    if len(name) == name.count('A'):
        return 0
    for alpa in name:
        num_alpa = ord(alpa)
        
        if  num_alpa<= ((num_alpa+13-ord('A'))%26+ord('A')): # a~n 일 경우 위로 조작
            answer += num_alpa-ord('A')
            if alpa == 'A':
                AList.append(1)
            else:
                AList.append(0)
        else: # O~Z 일 경우 아래로 조작
            answer += ord('Z')-num_alpa+1
            AList.append(0)
        index += 1
    
    
    
    print(AList)
print(solution("AABAA"))

'''
ABABABABAAAA -> 4 + 8 = 12
CAABAD -> 5 + 4
[0,3,6]

BBBAAAB -> 9
ABABAAAAABA -> 11

'''
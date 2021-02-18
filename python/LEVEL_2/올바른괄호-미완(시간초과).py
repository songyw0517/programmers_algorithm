def solution(s):
    stack = []
    print()
    if s[0] == ')' or s[len(s)-1] == '(' or list(s).count(')') >= (len(s)/2)+1 or list(s).count('(') >= (len(s)/2)+1:
        return False
    leftLimit = 0
    for i in s:
        if leftLimit > len(s)/2+1:
            return False
        if i == ')': # 닫혀있는 것이 들어오면
            if stack == []:
                return False
            elif stack[0] == '(':
                leftLimit +=1
                stack.pop(0)
            else:
                return False
        else:
            stack.insert(0, i)
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    if stack == []:
        return True
    else:
        return False
print(solution("(((((((((((((((((()"))
'''
test data
(())()
)
// ()
)
))
) // ()
//()

시간초과


def solution(s):
    
'''
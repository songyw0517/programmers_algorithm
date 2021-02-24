def solution(s):
    stack = []
    top = 0
    if s[0] == ')' or s[len(s)-1] == '(' or list(s).count(')') != list(s).count('(') or list(s).count('(') > int(len(s)/2)+1 or list(s).count(')') > int(len(s)/2)+1:
        return False
    for i in s:
        if i == ')': # 닫혀있는 것이 들어오면
            if stack == []:
                return False
            else:
                try:
                    if stack[top] != '(':
                        return False
                    else:
                        top+=1
                except:
                    return False
        else:
            stack.append(i)
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    return True
print(solution("(())"))
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
    stack = []
    print()
    if s[0] == ')' or s[len(s)-1] == '(' or list(s).count(')') != list(s).count('(') or list(s).count('(') > int(len(s)/2)+1 or list(s).count(')') > int(len(s)/2)+1:
        return False
    for i in s:
        if i == ')': # 닫혀있는 것이 들어오면
            if stack == []:
                return False
            else:
                stack.pop(0)
        else:
            stack.insert(0, i)
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    if stack == []:
        return True
    else:
        return False
'''
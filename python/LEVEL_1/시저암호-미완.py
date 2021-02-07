def solution(s, n):
    answer = ''
    S = list(s)
    for i in S:
        if i>='a' and i<='z': #소문자인 경우
            (i) += n
        elif i>='A' and i<='Z': #대문자인 경우
            i += n
    print(S)
    
    return answer
print(solution("AB", 1))
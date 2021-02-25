def solution(number, k):
    answer = ''
    number_len = len(number)-k
    while k>0:
        if len(answer)>=number_len:
            return answer
        index = number.index(max(number[0:k+1]))
        if number[index]=='9' and k==1:
            return answer+number[:len(number)-1]
        answer+=number[index]
        k-=index
        number = number[index+1:]
    
    return answer+number

#print(solution("4177252841",4))
print(solution("9999991",4))

'''

'''
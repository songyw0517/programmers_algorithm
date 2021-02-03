def solution(number, k):
    answer = ''
    number = list(number)
    for i in range(k):
        number.pop(number.index(min(number)))
    return number
print(solution("4177252841",4))
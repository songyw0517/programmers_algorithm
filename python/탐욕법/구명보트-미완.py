def solution(people, limit):
    answer = 0
    people.sort()
    for i, value in enumerate(people[:]):
        people.pop(0)
        print(value)
    return answer

print(solution([20, 30, 60, 80], 100))

'''
50      
70 80
sum = 50

80
70
sum = 120
-> sum = 80

70
[]
sum = 150



20 30 60 80 , 100-> 2가 나와야 한다.


탐욕법 2가지 방법이 있다

'''
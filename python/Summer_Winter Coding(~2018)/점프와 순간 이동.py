# DFS같다

def solution(n):
    ans = n # 건전지 사용량, 최대값, 바로 점프하는 경우
    for i in range(1, n):
        print('i = ', i)
        distance = temp_ans = i # i칸 점프
        while distance < n: # 순간이동
            distance = distance*2
        if distance > n:
            distance/=2
        print(distance)
        temp_ans += n-distance
        print("temp = ", temp_ans)
        if temp_ans < ans:
            ans=temp_ans
    return int(ans)
print(solution(6))


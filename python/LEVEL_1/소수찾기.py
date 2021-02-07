def solution(n):
    answer = 0
    '''
    for i in range(2, n+1):
        flag=True
        for j in range(2, (i//2)+1):
            if i%j==0:
                flag = False
                break
        if flag:
            answer+=1
    return answer
    '''
    prime_list = [True]*(n+1) # n+1개만큼 True 리스트 생성
    
    for i in range(2, int(n**0.5)+1): # 2부터 루트n에 1을 더한것까지 반복문을 시킴  2~3까지인디
        #if prime_list[i] == True:
        for j in range(i+i, n+1, i): # 4~5를 False로 바꾼다? 4만 false로 바뀜
                # i+i = i*2이니까 자기자신의 2배로 나누어져서 소수가 아니다. 이거를 배열에 처 담는다?
            prime_list[j]=False # 코드외워야겠다 슈벨
    #print(prime_list)
    return (len([i for i in range(2, n+1) if prime_list[i]==True])) # 2~n+1까지
print(solution(5))
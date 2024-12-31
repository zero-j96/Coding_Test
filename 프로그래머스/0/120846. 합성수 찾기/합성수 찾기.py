def solution(n):
    answer = 0
    i=2
    while i <= n:
        for j in range(2,i):
            if i % j == 0:
                answer +=1
                break
        i +=1
    return answer
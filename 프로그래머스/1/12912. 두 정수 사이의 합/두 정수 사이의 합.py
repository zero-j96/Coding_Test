def solution(a, b):
    answer =0
    for i in range(min(a,b),max(a+1,b+1)):
        answer += i
    return answer 
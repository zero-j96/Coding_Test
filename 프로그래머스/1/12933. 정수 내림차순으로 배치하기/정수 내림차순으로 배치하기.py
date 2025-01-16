def solution(n):
    answer =''
    for i in range(1,len(str(n))+1):
        answer += sorted(str(n))[-i]
    return int(answer)
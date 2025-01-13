def solution(n):
    answer = 0
    for i in range(len(str(n))):
        a = str(n)[i]
        answer += int(a)
    return answer
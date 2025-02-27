def solution(n):
    answer = 0
    fact = 1
    while n >= fact:
        answer += 1
        fact *= answer
        
    return answer-1
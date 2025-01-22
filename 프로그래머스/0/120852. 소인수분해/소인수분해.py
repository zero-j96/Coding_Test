def solution(n):
    answer = []
    i = 2
    while i <= n:
        if n % i ==0:
            answer.append(i)
            n /= i
            i = 2
        else:
            i += 1
    answer = list(set(answer))
    return sorted(answer)
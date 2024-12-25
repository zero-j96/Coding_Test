def solution(n):
    a =0
    for i in range(len(str(n))-1,-1,-1):
        a += n // (10**i)
        n = n % (10**i)
    return a
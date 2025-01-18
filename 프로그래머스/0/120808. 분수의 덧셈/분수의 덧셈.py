def solution(numer1, denom1, numer2, denom2):
    answer = []
    a = denom1 * denom2
    b = numer1 * denom2 + numer2 * denom1
    for i in range(min(a,b),1,-1):
        if (a % i ==0) & (b % i ==0):
            a /= i
            b /= i
    answer = [b,a]     
    return answer
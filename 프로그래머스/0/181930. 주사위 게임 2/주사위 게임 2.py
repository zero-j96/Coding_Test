def solution(a, b, c):
    answer = 0
    if (a == b) & (b== c) &(c==a):
        return (a+b+c) * (a**2 +b**2+c**2) *(a**3 + b**3 + c**3)
    elif (a !=b) & (b !=c) & (c!=a):
        return (a+b+c)
    else:
        return(a+b+c) * (a**2+b**2+c**2)
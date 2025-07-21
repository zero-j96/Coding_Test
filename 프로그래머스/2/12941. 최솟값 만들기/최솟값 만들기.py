def solution(A,B):
    sum = 0
    for i,j in zip(sorted(A), sorted(B, reverse = True)):
        sum += i*j
    return sum
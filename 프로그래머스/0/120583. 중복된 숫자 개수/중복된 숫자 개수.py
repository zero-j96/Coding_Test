def solution(array, n):
    a= 0
    for i in range(len(array)):
        if n == array[i]:
            a+=1
    return a
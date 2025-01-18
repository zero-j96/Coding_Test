def solution(array, n):
    a =[]
    b= []
    for i in range(len(array)):
        a.append(abs(n - array[i]))
    for j in range(len(array)):
        if a[j] == min(a):
            b.append(array[j])
    return min(b)
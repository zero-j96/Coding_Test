def solution(quiz):
    answer = []
    for i in range(len(quiz)):
        a = quiz[i].split()
        if a[1] == '+':
            b = int(a[0]) + int(a[2])
            if b == int(a[4]):
                answer.append('O')
            else:
                answer.append('X')
        else:
            b = int(a[0]) - int(a[2])
            if b == int(a[4]):
                answer.append('O')
            else:
                answer.append('X')
    return answer
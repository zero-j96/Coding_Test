def solution(dots):
    a = [[[0,1],[2,3]],[[0,2],[1,3]],[[0,3],[1,2]]]
    for k in range(3):
        b = []
        for i, j in a[k]:
            b.append((dots[i][1] - dots[j][1]) / (dots[i][0] -dots[j][0]))
        if b[0] == b[1]:
            return 1
    return 0
                     
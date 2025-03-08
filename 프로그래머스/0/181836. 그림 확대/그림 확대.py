def solution(picture, k):
    answer = []
    for i in range(len(picture)):
        a =""
        for j in range(len(picture[i])):
            a += picture[i][j] * k
        for l in range(k):
            answer.append(a)
    return answer
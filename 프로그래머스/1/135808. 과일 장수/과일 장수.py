def solution(k, m, score):
    answer = []
    count = 0
    a = sorted(score)[::-1]
    for i in range(len(score)//m):
        b=[]
        for j in range(m*i,m*(i+1)):
            b.append(a[j])
        answer.append(b)
    for k in range(len(answer)):
        count += (min(answer[k]) * m)
    
    return count
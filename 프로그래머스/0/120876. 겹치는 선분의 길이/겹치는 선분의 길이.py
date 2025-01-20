def solution(lines):
    answer = 0
    ls =[]
    for i in range(3):
        for j in range(lines[i][0],lines[i][1]):
            ls.append(j)
            
    for k in range(min(ls),max(ls)+1):
        if ls.count(k) >= 2:
            answer += 1
    return answer
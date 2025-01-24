def solution(n, m, section):
    answer = 0
    i = section[0]
    if m == 1:
        return len(section)
    elif m ==2:
        return len(section)//2
    else:
        while i <= section[-1]:
            if i not in section:
                i += 1
            else:
                answer += 1
                i += m
        return answer
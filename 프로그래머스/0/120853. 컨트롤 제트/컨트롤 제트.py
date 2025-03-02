def solution(s):
    answer = 0
    if 'Z' in s:
        s = s.replace(' Z','Z')
    s = s.split()
    for i in s:
        if "Z" in i:
            continue
        else:
            answer += int(i)
    return answer
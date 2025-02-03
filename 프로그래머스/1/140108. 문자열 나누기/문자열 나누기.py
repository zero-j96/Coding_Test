def solution(s):
    answer = 0
    i = 0
    s1 = ''
    while i < len(s):
        s1 += (s[i:i+2])
        if s1.count(s1[0]) == len(s1) - s1.count(s1[0]):
            answer += 1
            s1 = ''
            i += 2
        elif (len(s)-2 <= i) &(s1.count(s1[0]) != len(s1) -s1.count(s1[0])):
            answer += 1
            i += 2
        else:
            i += 2
    return answer
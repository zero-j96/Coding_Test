def solution(myString, pat):
    a =''
    for i in range(len(pat)):
        if pat[i] == 'A':
            a += 'B'
        else:
            a += 'A'
    return 1 if a in myString else 0
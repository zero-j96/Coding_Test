def solution(rsp):
    answer = ''
    for i in range(len(rsp)):
        if rsp[i] == '2':
            answer += '0'
        elif rsp[i] == '5':
            answer += '2'
        else:
            answer += '5'
    return answer
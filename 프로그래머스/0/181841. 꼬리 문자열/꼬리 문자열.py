def solution(str_list, ex):
    answer = ''
    for i in range(len(str_list)):
        if ex in str(str_list[i]):
            continue
        else:
            answer += str(str_list[i])
    return answer
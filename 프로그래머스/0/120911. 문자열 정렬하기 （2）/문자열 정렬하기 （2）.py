def solution(my_string):
    answer = ''
    for i in range(len(my_string)):
        answer += sorted(my_string.lower())[i]
    return answer
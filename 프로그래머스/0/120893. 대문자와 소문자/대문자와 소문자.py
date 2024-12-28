def solution(my_string):
    answer = ''
    for i in range(len(my_string)):
        if my_string[i] == my_string[i].lower():
            answer += my_string[i].upper()
        else:
            answer += my_string[i].lower()
    return answer
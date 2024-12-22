def solution(my_string):
    sum =0
    for i in range(len(my_string)):
        for j in range(10):
            if f'{j}' == my_string[i]:
                sum += j
    answer = sum
    return answer
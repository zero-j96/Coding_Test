def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        for j in range(10):
            if my_string[i] == f"{j}":
                answer.append(j)
    return sorted(answer)
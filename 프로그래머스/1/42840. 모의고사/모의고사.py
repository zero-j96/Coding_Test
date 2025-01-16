def solution(answers):
    count_1 = 0
    count_2 = 0
    count_3 = 0
    answer_1 = [1,2,3,4,5] * ((len(answers) // 5) + 1)
    answer_2 = [2,1,2,3,2,4,2,5] * ((len(answers) // 8) + 1)
    answer_3 = [3,3,1,1,2,2,4,4,5,5] * ((len(answers) // 10)+ 1)
    for i in range(len(answers)):
        if answers[i] == answer_1[i]:
            count_1 += 1
        if answers [i] == answer_2[i]:
            count_2 += 1
        if answers[i] == answer_3[i]:
            count_3 += 1
    answer = []
    if max(count_1, count_2, count_3) == count_1:
        answer.append(1)
    if max(count_1, count_2, count_3) == count_2:
        answer.append(2)
    if max(count_1, count_2, count_3) == count_3:
        answer.append(3)
    return sorted(answer)
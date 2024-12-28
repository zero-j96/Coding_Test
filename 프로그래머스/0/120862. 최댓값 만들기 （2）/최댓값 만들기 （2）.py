def solution(numbers):
    answer = sorted(numbers)
    answer1 = answer[-1]*answer[-2]
    answer2 = answer[0]*answer[1]
    return max(answer1,answer2)
def solution(array, height):
    answer = 0
    for i in range(len(array)):
        if height < sorted(array)[i]:
            answer += 1
    return answer
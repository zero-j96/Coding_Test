def solution(array):
    answer = []
    for i in range(len(array)):
        if array[i] == max(array):
            answer = [array[i],i]
    return answer
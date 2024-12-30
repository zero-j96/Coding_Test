def solution(arr, intervals):
    answer = []
    answer1 = []
    for i in range(len(intervals)):
        answer.append(arr[intervals[i][0]:intervals[i][1]+1])
    for i in range(len(answer)):
        for j in range(len(answer[i])):
            answer1.append(answer[i][j])
    return answer1
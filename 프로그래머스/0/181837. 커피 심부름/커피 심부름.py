def solution(order):
    answer = 0
    for i in range(len(order)):
        if "latte" in order[i]:
            answer += 5000
        else:
            answer += 4500
    return answer
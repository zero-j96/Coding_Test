def solution(sides):
    small = 0
    big = 0
    count = 0
    answer = 0
    
    for i in range(3):
        if sides[i] < max(sides):
            small += sides[i]
        else:
            big += sides[i]
            count += 1
    
    if count >=2:
        answer =1
    elif big >= small:
        answer =2
    else:
        answer =1
    return answer
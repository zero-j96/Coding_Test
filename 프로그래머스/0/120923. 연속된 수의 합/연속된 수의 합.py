def solution(num, total):
    answer = []
    if total % num ==0:
        answer.append(total //num)
        for i in range(1,num//2 + 1):
            answer.append(total//num + i)
            answer.append(total//num - i)
    else:
        for i in range(num):
            answer.append((total//num + num//2)-i)
        
    return sorted(answer)
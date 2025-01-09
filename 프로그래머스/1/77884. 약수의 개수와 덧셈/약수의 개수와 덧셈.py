def solution(left, right):
    answer =0
    list_num =[]
    num =[]
    a = 0
    for i in range(left,right+1):
        num.append(i)
        answer=0
        for j in range(1,i+1):
            if i % j ==0:
                answer +=1
        list_num.append(answer)
    for j in range(len(list_num)):
        if list_num[j] % 2 ==0:
            a += num[j]
        else:
            a -= num[j]
    
    return a
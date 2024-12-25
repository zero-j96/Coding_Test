def solution(num_list):
    prod = 1
    total = 0
    for i in range(len(num_list)):
        prod *= num_list[i]
        total += num_list[i]
    if prod < total**2:
        answer = 1
    else:
        answer = 0 
    return answer
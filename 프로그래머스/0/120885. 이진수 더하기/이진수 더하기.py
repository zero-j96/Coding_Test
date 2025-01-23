def solution(bin1, bin2):
    answer = ''
    num = int(bin1) + int(bin2)
    num1 = 0
    for i in range(len(str(num))):
        num1 += (num % 10) * (2**i)
        num = num // 10
    if num1 == 0:
        answer ='0'
    while num1 > 0:
        answer += str(num1 % 2)
        num1 = num1 // 2
    return answer[::-1]
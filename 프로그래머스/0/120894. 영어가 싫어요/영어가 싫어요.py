def solution(numbers):
    answer = 0
    a = ['zero','one','two','three','four','five','six','seven','eight','nine']
    b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i,j in zip(a,b):
        numbers = numbers.replace(i,str(j))
    return int(numbers)
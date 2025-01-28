import math
def solution(my_str, n):
    return [my_str[n * i: n * (i+1)] for i in range(math.ceil(len(my_str)/n))]
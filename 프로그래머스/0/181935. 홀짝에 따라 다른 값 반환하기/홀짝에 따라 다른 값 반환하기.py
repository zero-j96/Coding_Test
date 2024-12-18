
def solution(n):
    a = 0
    if n %2 == 1:
        for i in range(n,0,-2):
            a+=i
    
    else:
        for j in range(n,0,-2):
            a+= (j**2)
            
    return a
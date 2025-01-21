def solution(s):
    list_num =['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in range(10):
        if list_num[i] in s:
            s = s.replace(str(list_num[i]),str(i))
    
    return int(s)
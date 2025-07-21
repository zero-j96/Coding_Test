def solution(s):
    if s[0] == ")" or s[-1] == "(":
        return False
    num = 0
    for i in s:
        if i == "(":
            num += 1
        else:
            num -= 1
        if num < 0:
            return False
    if num == 0:
        return True
    else:
        return False
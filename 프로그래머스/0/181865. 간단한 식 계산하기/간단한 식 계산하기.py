def solution(binomial):
    a, b = int(binomial.split(' ')[0]), int(binomial.split(' ')[-1])
    op = binomial.split(' ')[1]
    if op == '+':
        return a+b
    elif op =='-':
        return a-b
    else:
        return a *b
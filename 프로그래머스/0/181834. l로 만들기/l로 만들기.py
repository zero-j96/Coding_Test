def solution(myString):
    answer = ''
    a = ['a','b','c','d','e','f','g','h','i','j','k']
    for i in range(len(a)):
        if a[i] in myString:
            myString = myString.replace(a[i],'l')
    return myString
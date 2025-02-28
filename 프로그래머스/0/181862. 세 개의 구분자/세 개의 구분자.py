def solution(myStr):
    answer = []
    myStr = myStr.replace("a"," ").replace("b"," ").replace("c"," ").strip().split(" ")
    for i in range(len(myStr)):
        if len(myStr[i]):
            answer.append(myStr[i])
    if myStr == [""]:
        answer = ["EMPTY"]
    return answer
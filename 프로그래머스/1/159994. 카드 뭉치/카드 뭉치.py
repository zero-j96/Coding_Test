def solution(cards1, cards2, goal):
    answer1 = []
    answer2 = []
    for i in range(len(cards1)):
        if cards1[i] in goal:
            answer1.append(goal.index(cards1[i]))
        else:
            break
            
    for j in range(len(cards2)):
        if cards2[j] in goal:
            answer2.append(goal.index(cards2[j]))
        else:
            break
    if len(answer1) + len(answer2) != len(goal):
        return "No"
    elif answer1 == sorted(answer1) and answer2 == sorted(answer2):
        return "Yes"
    else:
        return "No"
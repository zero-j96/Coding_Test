def solution(babbling):
    bab_li = ["aya","ye","woo","ma"]
    for i in range(len(babbling)):
        for bab in bab_li:
            if babbling[i].count(bab) > 1:
                break
            elif babbling[i].count(bab) == 1:
                babbling[i] = babbling[i].replace(bab,' ')
            else:
                continue
            babbling[i]= babbling[i].strip()
    return babbling.count("")
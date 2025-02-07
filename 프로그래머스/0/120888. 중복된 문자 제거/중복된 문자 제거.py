def solution(my_string):
    answer = ''
    i=0
    while i < len(my_string):
        if my_string[i] in my_string[i+1:]:
            my_string = my_string[:i+1]+my_string[i+1:].replace(my_string[i],'')
        else:
            i += 1
    return my_string
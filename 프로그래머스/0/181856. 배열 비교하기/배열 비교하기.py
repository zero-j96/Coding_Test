def solution(arr1, arr2):
    if len(arr1)>len(arr2):
        return 1
    elif len(arr1) == len(arr2):
        if sum(arr1) > sum(arr2):
            return 1
        elif sum(arr2) > sum(arr1):
            return -1
        else:
            return 0
    else:
        return -1
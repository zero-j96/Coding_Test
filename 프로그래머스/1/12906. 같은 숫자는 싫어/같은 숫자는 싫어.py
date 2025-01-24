def solution(arr):
    return [arr[i] for i in range(len(arr)) if arr[i-1] != arr[i] or i==0]
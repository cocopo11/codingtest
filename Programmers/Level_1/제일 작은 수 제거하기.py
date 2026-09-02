def solution(arr):
    a = min(arr)
    del arr[arr.index(a)]
    if len(arr) == 0:
        return [-1]
    return arr
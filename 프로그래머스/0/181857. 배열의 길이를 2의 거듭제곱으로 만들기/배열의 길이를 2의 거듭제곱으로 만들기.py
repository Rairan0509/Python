def solution(arr):
    i = 1
    while len(arr) != i:
        if len(arr) > i:
            i *= 2
        else:
            arr.extend([0]*(i - len(arr)))
            break
    return arr
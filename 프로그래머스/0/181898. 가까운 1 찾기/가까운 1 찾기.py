def solution(arr, idx):
    while idx < len(arr):
        if arr[idx] == 0:
            idx += 1
        else:
            return idx
    return -1
        
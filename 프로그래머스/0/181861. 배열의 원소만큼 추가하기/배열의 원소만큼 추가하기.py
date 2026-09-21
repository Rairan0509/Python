def solution(arr):
    arr1 = []
    for num in arr:
        arr1.extend([num]*num)
    return arr1 
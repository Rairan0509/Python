def solution(arr):

    for arr1 in arr:
        if len(arr) > len(arr1):
            for _ in range(len(arr)-len(arr1)):
                arr1.append(0)
    if len(arr[0]) > len(arr):
        for _ in range(len(arr[0])-len(arr)):
            arr.append([0]*len(arr[0]))
    return arr
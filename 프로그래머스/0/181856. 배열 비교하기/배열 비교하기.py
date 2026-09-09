def solution(arr1, arr2):
    if len(arr1) != len(arr2):
        if len(arr1) > len(arr2):
            return 1
        else:
            return -1
    elif len(arr1) == len(arr2):
        arr1_total = 0
        arr2_total = 0
        for i in range(len(arr1)):
            arr1_total += arr1[i]
            arr2_total += arr2[i]
    if arr1_total > arr2_total:
            return 1
    elif arr1_total < arr2_total:
            return -1
    else:
            return 0

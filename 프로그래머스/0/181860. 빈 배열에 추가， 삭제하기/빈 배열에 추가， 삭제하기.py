def solution(arr, flag):
    arr1 = []
    for i in range(len(arr)):
        if flag[i] == True:
            arr1.extend([arr[i]]*arr[i]*2)
        else:
            del arr1[-arr[i]:]
    return arr1
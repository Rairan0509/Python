def solution(arr, k):
    if k % 2 == 1:
        arr1 = []
        for number in arr:
            arr1.append(number * k)
        return arr1
    else:
        arr1 = []
        for number in arr:
            arr1.append(number + k)
        return arr1
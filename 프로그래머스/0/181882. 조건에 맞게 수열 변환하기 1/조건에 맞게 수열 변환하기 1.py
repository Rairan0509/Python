def solution(arr):
    arr1 = []
    for num in arr:
        if num >= 50 and num % 2 == 0:
            number = num // 2
            arr1.append(number)

        elif num < 50 and num % 2 == 1:
            number = num * 2
            arr1.append(number)

        else: 
            arr1.append(num)
    return arr1
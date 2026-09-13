def solution(arr):
    number = []
    for i in range(len(arr)):
        if arr[i] == 2:
            number.append(i)
    
    if not number:
        return [-1]
            
    return arr[number[0]:number[-1]+1]
        
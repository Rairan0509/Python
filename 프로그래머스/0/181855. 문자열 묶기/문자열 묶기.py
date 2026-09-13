def solution(strArr):
    count = {}
    for arr in strArr:
        length = len(arr)
        if length in count:
            count[length] +=1
        else:
            count[length] = 1

    total = 0
    for value in count.values():
        if value > total:
            total = value

    return total
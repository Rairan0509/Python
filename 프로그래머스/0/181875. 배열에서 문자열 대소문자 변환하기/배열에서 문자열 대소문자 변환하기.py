def solution(strArr):
    result = []
    for idx in range(len(strArr)):
        if idx % 2 == 0:
            result.append(strArr[idx].lower())
        else:
            result.append(strArr[idx].upper())
    return result

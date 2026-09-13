def solution(intStrs, k, s, l):
    number = []
    for intStr in intStrs:
        if int(intStr[s:s+l]) > k:
            number.append(int(intStr[s:s+l]))
    return number
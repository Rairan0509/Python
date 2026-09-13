def solution(myString, pat):
    n = len(pat)
    count = 0
    for i in range(len(myString)):
        if pat in myString[i:i+n]:
            count +=1
    return count
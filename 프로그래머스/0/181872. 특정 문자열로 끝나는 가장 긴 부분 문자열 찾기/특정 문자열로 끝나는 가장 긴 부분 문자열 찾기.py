def solution(myString, pat):
    i = len(pat)
    last = -1
    for j in range(len(myString)):
        if myString[j:j+i] == pat:
            last = j
    return myString[:last+i]
def solution(strArr):
    strarr =[]
    for word in strArr:
        if "ad" not in word:
            strarr.append(word)
    return strarr
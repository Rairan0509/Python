def solution(numLog):
    word = ""
    num = len(numLog) - 1
    while num > 0:
        if numLog[num]-numLog[num-1] == 1:
            word = "w" + word
            num -= 1
        elif numLog[num]-numLog[num-1] == -1:
            word = "s" +word
            num -= 1
        elif numLog[num]-numLog[num-1] == 10:
            word = "d" + word
            num -= 1
        elif numLog[num]-numLog[num-1] == -10:
            word = "a" + word
            num -= 1
    return word
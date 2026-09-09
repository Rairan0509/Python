def solution(myString, pat):
    String = myString.replace("A", "C")
    String1 = String.replace("B", "A")
    String2 = String1.replace("C", "B")
    if pat in String2:
        return 1
    else:
        return 0
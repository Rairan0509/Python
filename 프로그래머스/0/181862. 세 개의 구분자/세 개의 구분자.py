def solution(myStr):
    result = []
    temp = ""

    for ch in myStr:
        if ch in ["a", "b", "c"]:
            if temp:
                result.append(temp)
            temp = ""
        else:
            temp += ch     
    if temp:
        result.append(temp)
    if not result:
        result = ["EMPTY"]
    return result
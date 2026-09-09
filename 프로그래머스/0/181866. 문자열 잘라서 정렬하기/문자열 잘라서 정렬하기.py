def solution(myString):
    string = myString.split("x")
    result = list(filter(lambda x: x !="",string))
    return sorted(result)
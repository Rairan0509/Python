def solution(myString):
    string = myString.split("x")
    x_list = []
    for word in string:
        x_list.append(len(word))
    return x_list

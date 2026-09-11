def solution(my_string, m, c):
    string = []
    for i in range(0, len(my_string), m):
        string.append(my_string[i:i+m])
    stri = ""
    for word in string:
        stri += word[c-1]
    return stri
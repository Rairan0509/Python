def solution(my_string):
    string = []
    for i in range(len(my_string)):
        string.append(my_string[i:len(my_string)])
    return sorted(string)
def solution(my_string, index_list):
    word = ""
    for number in index_list:
        word += my_string[number]
    return word
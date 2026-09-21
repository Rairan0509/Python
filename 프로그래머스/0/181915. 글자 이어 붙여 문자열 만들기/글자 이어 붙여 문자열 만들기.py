def solution(my_string, index_list):
    word = ""
    for idx in index_list:
        word += my_string[idx]
    return word

def solution(my_string, is_suffix):
    if my_string[-len(is_suffix):] == is_suffix[0:]:
        return 1
    else:
        return 0

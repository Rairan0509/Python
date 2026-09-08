def solution(str_list, ex):
    answer = ""
    for str1 in str_list:
        if ex not in str1:
            answer += str1
    return answer
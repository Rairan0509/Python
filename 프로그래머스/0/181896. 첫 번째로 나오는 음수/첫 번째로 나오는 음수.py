def solution(num_list):
    for number in range(len(num_list)):
        if num_list[number] < 0 :
            return number
    return -1

print(solution([12, 4, 15, 46, 38, -2, 15]))
def solution(num_list):
    total = 0
    multi = 1
    for number in num_list:
        total += number
        multi *= number
    if multi < total**2 :
        return 1
    return 0
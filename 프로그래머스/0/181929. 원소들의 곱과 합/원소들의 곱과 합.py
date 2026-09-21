def solution(num_list):
    sum = 0
    multiple = 1
    for num in num_list:
        sum += num
        multiple *= num

    if multiple < sum**2:
        return 1
    else:
        return 0
def solution(num_list):
    num_list2 = []
    for number in num_list:
        num_list2.append(number)
    
    if num_list[-1] > num_list[-2]:
        num_list2.append(num_list[-1]-num_list[-2])
    else:
        num_list2.append(num_list[-1]*2)

    return num_list2
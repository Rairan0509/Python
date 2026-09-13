def solution(num_list):
    total = 0
    for number in num_list:
        result = 0
        while number != 1:
            if number % 2 == 0:
                number = number // 2
                result += 1
            else:
                number = (number - 1) // 2
                result += 1
        total += result
    return total
def solution(number):
    total = 0
    for num in number:
        total += int(num)
    return total % 9
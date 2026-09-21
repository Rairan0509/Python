def solution(n):
    if n % 2 == 1:
        total = 0
        for i in range(1, n+1, 2):
            total += i
        return total
    elif n % 2 == 0:
        total = 0
        for i in range(2, n+1, 2):
            total += i**2
        return total

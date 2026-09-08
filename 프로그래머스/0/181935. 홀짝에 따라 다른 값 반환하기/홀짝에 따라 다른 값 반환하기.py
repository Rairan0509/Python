def solution(n):
    if n % 2 == 1:
        total = 0
        for i in range(1, n+1):
            if i % 2 == 1:
                total +=i
    else:
        total = 0
        for i in range(1, n+1):
            if i % 2 == 0:
                total += i**2
    return total
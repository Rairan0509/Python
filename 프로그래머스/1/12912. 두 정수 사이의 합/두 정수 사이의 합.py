def solution(a, b):
    
    if a == b:
        return a
    
    total = 0
    if a > b:
        for i in range(b, a+1):
            total +=i
        return total
    else:
        for i in range(a, b+1):
            total += i
        return total
def solution(n):
    X = []
    while n != 1:
        X.append(n)
        
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
            
    X.append(1)
    return X
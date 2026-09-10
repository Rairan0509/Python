def solution(n, k):
    number = []
    for i in range(1,n+1):
        if i % k == 0:
            number.append(i)
    return number
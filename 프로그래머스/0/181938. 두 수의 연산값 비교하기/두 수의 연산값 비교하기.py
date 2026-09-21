def solution(a, b):
    total = int(str(a)+str(b))
    if  total > 2*a*b:
        return total
    elif total < 2*a*b:
        return 2*a*b
    else:
        return total
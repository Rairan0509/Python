def solution(n):
    n =str(n)

    number = ""
    for i in reversed(sorted(n)):
        number += i
    
    return int(number)
def solution(order):
    total = 0
    for coffee in order:
        if "americano" in coffee:
            total += 4500
        elif "cafelatte" in coffee:
            total += 5000
        else:
            total += 4500
    return total
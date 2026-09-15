def solution(l, r):

    results = []
    for i in range(1,65):
        binary = bin(i)[2:]
        changed = int(binary.replace("1", "5"))
        if l <= changed <= r:
            results.append(changed)
    
    if results:
        return results
    else:
        return [-1]
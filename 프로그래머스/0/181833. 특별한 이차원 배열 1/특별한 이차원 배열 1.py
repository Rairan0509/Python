def solution(n):
    row = []
    for i in range(n):
        col = []
        for j in range(n):
            if i == j:
                col.append(1)
            else:
                col.append(0)
        row.append(col)
    return row
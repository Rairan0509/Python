def solution(rank, attendance):
    rank_true = {}
    for i in range(len(rank)):
        if attendance[i] :
            rank_true[rank[i]] = i

    top3 = sorted(rank_true.items())[:3]
    a = top3[0][1]
    b = top3[1][1]
    c = top3[2][1]
    return 10000 * a + 100 * b + c
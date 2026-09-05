p = []
h, w = map(int, input().split())

for i in range(h):
    board = []

    for row in range(w):
        board.append(0)

    p.append(board)

stick = int(input())

for count in range(stick):
    l, d, x, y = map(int, input().split())

    x = x - 1
    y = y - 1

    for position in range(l):

        if d == 0:
            p[x][y + position] = 1

        else:
            p[x + position][y] = 1

for i in range(h):
    for j in range(w):
        print(p[i][j], end = " ")

    print()

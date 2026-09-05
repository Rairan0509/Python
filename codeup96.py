# 96번
board = []

for i in range(19):
    row = list(map(int, input().split()))
    board.append(row)                       #바둑판을 만드는 과정

num = int(input())

for count in range(num):
    x, y = map(int, input().split())        #뒤집는 횟수
    x = x - 1
    y = y - 1

    for column in range(19):                #x행 뒤집기 시작
        if board[x][column] == 0:
            board[x][column] = 1
        else:
            board[x][column] = 0

    for row in range(19):                   #y행 뒤집기 시작
        if board[row][y] == 0:
            board[row][y] = 1

        else:
            board[row][y] = 0

for row in range(19):                       #결과 출력

    for column in range(19):
        print(board[row][column], end = " ")

    print()
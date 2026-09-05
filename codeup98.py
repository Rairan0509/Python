row = []

for w in range(10):
    board = list(map(int, input().split()))
    row.append(board)

ant_row = 1
ant_column = 1

while True:
    # 1) 먹이를 찾은 경우
    if row[ant_row][ant_column] == 2:
        row[ant_row][ant_column] = 9
        break

    if row[ant_row][ant_column] == 0:
        row[ant_row][ant_column] = 9

    # 2) 맨 아래의 가장 오른쪽에 도착한 경우
    if ant_row == 8 and ant_column == 8:
        break

    # 오른쪽으로 갈 수 있는지 확인
    if row[ant_row][ant_column + 1] == 0 or row[ant_row][ant_column + 1] == 2:
        ant_column = ant_column + 1
    # 오른쪽이 막혔으면 아래로 갈 수 있는지 확인
    elif row[ant_row + 1][ant_column] == 0 or row[ant_row + 1][ant_column] == 2:
        ant_row = ant_row + 1
    # 3) 더 이상 움직일 수 없는 경우
    else:
        break

for w in range(10):
    for h in range(10):
        print(row[w][h], end = " ")
    print()
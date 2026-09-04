d = []
for i in range(20): 
    d.append([])    #리스트안에 리스트
    for j in range(20): 
        d[i].append(0)

n = int(input())   
for i in range(n):
    x, y = input().split()
    d[int(x)][int(y)] = 1   #흰돌이 있는 위치 1,없는 곳 0

for i in range(1,20): #바둑판 가로
    for j in range(1,20): #바둑판 세로
        print(d[i][j],end = ' ') 
    print()

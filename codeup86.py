num = int(input())
# 1, 2, 3, 4, 5...순서대로 계속 더해가다가, 그 합이 입력된 정수보다 커지거나 같아지는 경우,
# 그때까지의 합을 출력한다.
# for문과 if문
total = 0
for i in range(1, num + 1):
        total += i
        if  total >= num :
            break
print(total)

# while문
total = 0
c = 1
while True:
    total += c
    c += 1
    if total >= num:
        break
print(total)
    

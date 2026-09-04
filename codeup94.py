n = int(input())
k = input().split()

for i in range(n):
    k[i] = int(k[i])
minimum = k[1]
for i in range(0, n):
    if k[i] < minimum :
        minimum = k[i]
print(minimum)
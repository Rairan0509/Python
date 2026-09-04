a = int(input())
i = 0

for s in range(1, a + 1):
    if s%2 == 0:
        i += s
print(i)
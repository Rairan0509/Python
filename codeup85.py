# w,h는 모두 정수
# b는 40이하의 4의배수
w, h, b = input().split()
w = int(w)
h = int(h)
b = int(b)
bit = w*h*b / 8  / 1024 / 1024
print(f"{bit:.2f}","MB")
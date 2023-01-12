a, b = map(int, input().split())
cnt = 1
while True:
    if a == b:
        print(cnt)
        break
    cnt += 1
    b = b + 1 if b < 999 else 0

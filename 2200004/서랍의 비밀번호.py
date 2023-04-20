p, k = map(int, input().split())
cnt = 1

while p != k:
    k+=1
    if k == 1000:
        k = 0
    cnt += 1

print(cnt)
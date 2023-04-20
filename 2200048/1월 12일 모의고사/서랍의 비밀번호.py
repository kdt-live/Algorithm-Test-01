k,p = 100, 123# map(int(input().split()))

cnt = 0

for i in range(k,p+1):
    cnt += 1
    if i == p:
        break

print(cnt)
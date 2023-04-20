# 2043 .서랍의 비밀번호
P, K = map(int, input().split())
cnt = 1

while True:
    if P == K:
        break
    else:
        cnt += 1
        K += 1
print(cnt)
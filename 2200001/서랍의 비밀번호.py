# 서랍의 비밀번호
P, K = map(int, input().split())
cnt = 0

for p in range(K, P+1):
    cnt += 1
    if p == P:
        print(cnt)
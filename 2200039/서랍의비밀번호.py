P, K = map(int, input().split()); cnt = 1
if P > K:
    while K != P:
        K += 1
        cnt += 1
elif P < K:
    while P != K:
        P += 1
        cnt += 1
elif P == K:
    pass
print(cnt)
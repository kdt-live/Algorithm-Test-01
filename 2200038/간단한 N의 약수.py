# N = 10

# for i in range(1, N+1):
#     if N % i == 0:
#         print(i, end=' ')

T = int(input())
for i in range(1, T+1):
    if T % i ==0:
        print(i, end=' ')

#서랍의 비밀번호
P, K = list(map(int,input().split()))

if P > K:
    print(P-K+1)

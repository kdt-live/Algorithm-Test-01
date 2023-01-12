# 홀수만 더하기
T = int(input())
for t in range(1, T+1):
    n = list(map(int, input().split()))
    cnt = 0
    for i in n:
        if i % 2 == 1:
            cnt += i
    print(f"#{t} {cnt}")
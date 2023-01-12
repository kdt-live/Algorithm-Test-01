# 2072 .홀수만 더하기

T = int(input())

for i in range(1, T+1):
    sum = 0
    num = list(map(int, input().split()))
    for j in num:
        if j % 2 == 1:
            sum += j
    
    print(f'#{i} {sum}')
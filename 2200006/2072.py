# 2072 .홀수만 더하기
T = int(input())

for tc in range(1, T + 1):
    sum = 0
    num = map(int, input().split())
    for i in num:
        if i % 2 == 1:
            sum += i
    print(f'#{tc} {sum}')
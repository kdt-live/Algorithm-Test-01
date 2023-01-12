# 2072
T = int(input())
odd = 0

for t in range(1, T+1):
    numbers = list(map(int, input().split()))
    for n in numbers:
        if n % 2 == 1:
            odd += n
    print(f'#{t} {odd}')
    odd = 0
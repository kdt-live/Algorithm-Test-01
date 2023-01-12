# 홀수만 더하기
T = int(input())
for t in range(1, T+1):
    numbers = list(map(int, input().split()))
    odd_sum = 0
    for i in numbers:
        if i % 2 == 1:
            odd_sum += i        
    print(f'#{t} {odd_sum}')
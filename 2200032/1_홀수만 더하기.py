# 1 (2072. 홀수만 더하기)
T = int(input())
for test_case in range(1, T+1):
    sum = 0
    lst = list(map(int, input().split()))
    for i in lst:
        if i & 1:            
            sum += i
    print(f'#{test_case} {sum}')
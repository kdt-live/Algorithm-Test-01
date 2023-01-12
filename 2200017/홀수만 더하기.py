#2072. 홀수만 더하기
T = int(input())

for test_case in range(1, T + 1):
    n = list(map(int, input().split()))
    sum = 0
    for j in n:
        if j%2 == 1:
            sum+=j
    print(f'#{test_case} {sum}')
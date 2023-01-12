T = int(input())
for test_case in range(1, T + 1):
    N = list(map(int, input().split()))
    result = 0
    for i in N:
        if i % 2 != 0:
            result += i
    print(f'#{test_case} {result}')

T = int(input())
for test_case in range(1, T + 1):
    numbers = list(map(int ,input().split()))
    odd = [i for i in numbers if i % 2 == 1]
    print(f'#{test_case} {sum(odd)}')
    
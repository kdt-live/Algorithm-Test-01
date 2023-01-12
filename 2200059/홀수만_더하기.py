# 1.홀수만 더하기


T = int(input())
for test_case in range(1, T + 1):
    nums = map(int, input().split())
    odd = []
    for i in nums:
        if i % 2 != 0:
            odd.append(i)
    result = sum(odd)

    print(f'#{test_case} {result}')

T = int(input())

for t in range(1, T+1):
    nums = list(map(int, input().split()))
    result = []

    for num in nums:
        if num % 2 == 1:
            result.append(num)

    print(f'#{t} {sum(result)}')
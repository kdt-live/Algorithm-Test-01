T = int(input())

for t in range(1, T+1):
    nums = list(map(int, input().split()))
    result = 0
    for i in nums:
        if i % 2:
            result += i
    print(f'#{t} {result}')
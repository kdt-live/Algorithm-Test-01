T = int(input())

for t in range(1, T + 1):
    nums = list(map(int, input().split()))
    cnt = 0
    for n in nums:
        if n%2 == 1:
            cnt += n
    print('#{} {}'.format(t, cnt))
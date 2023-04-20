case = int(input())

for i in range(1, case+1):
    nums = list(map(int, input().split()))
    result = [v for v in nums if v %2 != 0]
    print(f'#{i} {sum(result)}')
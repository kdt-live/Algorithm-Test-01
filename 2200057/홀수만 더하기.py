T = int(input())

for t in range(1, T+1):
    li = list(map(int, input().split()))
    sum = 0
    for l in li:
        if l % 2:
            sum += l
    print(f'#{t} {sum}')
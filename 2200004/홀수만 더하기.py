t = int(input())

for i in range(1, t+1):
    a = list(map(int,input().split()))
    odd_sum = 0
    for odd in a:
        if odd%2 == 1:
            odd_sum += odd
    print(f'#{i}', odd_sum)
T = int(input())
for t in range(1, T + 1):
    numbers = list(map(int,input().split()))
    for i in numbers:
        if i%2 == 1:
            result = 0
            result += i
            print(f'#{t} {result} ')
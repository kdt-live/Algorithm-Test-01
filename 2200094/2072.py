
T = int(input())

for t in range(1, T+1): 
    a = list(map(int, input().split()))
    result = 0
    for i in a:
        if i % 2 != 0:
            result += i
    print(f'#{t} {result}')
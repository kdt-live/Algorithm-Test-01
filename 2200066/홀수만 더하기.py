

T = int(input())



for t in range(1,T+1):
    total = 0
    numbers = list(map(int, input().split()))
    for num in numbers:
        if num % 2 == 1:
            total += num
    
    

    print(f'#{t} {total}')
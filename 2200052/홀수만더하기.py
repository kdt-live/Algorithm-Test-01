T = int(input())

for t in range(1, T+1):
    numbers = list(map(int,input().split()))
    sum = 0
    for n in numbers:
        if n % 2 == 1 :
            sum += n
    print(f"#{t} {sum}")
T=int(input())

for t in range(1, T+1):
    numbers = list(map(int,input().split()))
    sum=0
    for number in numbers :
        if number % 2 == 1:
            sum=number+sum
    print(f'#{t} {sum}')
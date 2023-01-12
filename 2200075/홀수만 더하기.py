T = int(input())

for t in range(1, T+1):
    numbers = map(int,input().split())
    holls = []
    for number in numbers :
        if 1 == number % 2 :
            holls.append(number)

    print(f'#{t} {sum(holls)}')
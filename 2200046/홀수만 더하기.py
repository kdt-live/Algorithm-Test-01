T = int(input())

for i in range(T):
    num = list(map(int, input().split()))
    result = 0
    for number in num:
        if number % 2 == 1:
            result += number
    print(f'#{i + 1} {result}')
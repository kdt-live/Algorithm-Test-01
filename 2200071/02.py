import datetime

T = int(input())
for t in range(1, T + 1):
    numbers = list(map(int,input().split()))
    for i in numbers:
        if datetime.date.month == 0:
                print(f'#{t} {datetime}')
        else:
                print(f'#{t} {-1}')
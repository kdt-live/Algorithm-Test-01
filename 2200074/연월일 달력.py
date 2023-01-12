T = int(input())

for t in range(1, T+1):
    date = input()

    year = date[:4]
    month = date[4:6]
    day = date[6:]

    if int(month) in [1, 3, 5, 7, 8, 10, 12]:
        if 0 < int(day) < 32:
            print(f'#{t} {year}/{month}/{day}')
        else:
            print(f'#{t} -1')
    elif int(month) == 2:
        if 0< int(day) < 29:
            print(f'#{t} {year}/{month}/{day}')
        else:
            print(f'#{t} -1')
    elif int(month) in [4, 6, 9, 11]:
        if 0 < int(day) < 31:
            print(f'#{t} {year}/{month}/{day}')
        else:
            print(f'#{t} -1')
    else:
        print(f'#{t} -1')

            
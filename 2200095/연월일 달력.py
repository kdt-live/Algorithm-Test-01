T = int(input())
for t in range(1, T + 1):
    input_ = input()
    year = (input_[0:4])
    month = (input_[4:6])
    day = (input_[6:8])
    if int(month) >= 13 or int(month) <= 0:
        print(f'#{t} -1')
    elif int(year) <= 0 :
        print(f'#{t} -1')
    elif int(day) <=0 or int(day) >= 32:
        print(f'#{t} -1')
    elif int(month) == 2:
        if int(day) >= 29:
            print(f'#{t} -1')
        else:
            print(f'#{t} {year}/{month}/{day}')
    elif int(month) == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        if int(day) >= 32:
            print(f'#{t} -1')
        else:
            print(f'#{t} {year}/{month}/{day}')
    elif int(month) == 4 or 6 or 9 or 11:
        if int(day) >= 31:
            print(f'#{t} -1')
        else:
            print(f'#{t} {year}/{month}/{day}')
    else:
        print(f'#{t} {year}/{month}/{day}')

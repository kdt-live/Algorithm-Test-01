T = int(input())

for i in range(T):
    date = input()
    date_year = date[:4]
    date_month = date[4:6]
    date_day = date[6:8]

    if int(date_month) <=0 or int(date_month) > 12:
        print(f'#{i} -1')
        continue
    
    if int(date_month) == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        if int(date_day) < 1 or int(date_day) > 31:
            print(f'#{i} -1')

    if date_month == 2:
        if int(date_day) < 1 or int(date_day) > 28:
            print(f'#{i} -1')

    if date_month == 4 or 6 or 9 or 11:
        if int(date_day) <= 0 or int(date_day) > 30:
            print(f'#{i} -1')

    print(f'{date_year}/{date_month}/{date_day}')
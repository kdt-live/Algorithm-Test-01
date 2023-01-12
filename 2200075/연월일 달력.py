T = int(input())

for t in range(1, T+1):
    nal = input()

    year_str = nal[0:4]
    year = int(nal[0:4])
    month_str = nal[4:6]
    month = int(nal[4:6])
    date_str = nal[6:8]
    date = int(nal[6:8])

    is_Year = year > 0
    is_Month = 1 <= month <= 12
    is_Date = 1 <= date <= 31

    if (month == 2) and (28 < date) or ((month==4 or month==6 or month==9 or month== 11) and (30 < date)):
        is_Date = False

    print(f'#{t}',end=' ')

    if(is_Date and is_Month and is_Year) :
        print(year_str,month_str,date_str,sep='/')
    else :
        print(-1)
# 연월일 달력
T = int(input())

for t in range(1, T + 1) :
    a = input()
    year = int(a[:4])
    month = int(a[4:6])
    day = int(a[6:8])

    if month == 1 or 3 or 5 or 5 or 8 or 10 or 12:
        if day <=31 :
            print(f'#{t} {year}/{month}/{day}')
        else :
            print('-1')    
    elif month == '4' or '6' or '9' or '11':
        if day <=30 :
            print(f'#{t} {year}/{month}/{day}')
        else :
            print('-1')            
    elif month == '2':
        if day <=28 :
            print(f'#{t} {year}/{month}/{day}')
        else :
            print('-1')
    else :
        print('-1')       
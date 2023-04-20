# 2056 .연월일 달력
T = int(input())

for i in range(1, T+1):
    num = input()
    lst = []
    lst_y = []
    lst_m = []
    lst_d = []
    year = 0
    month = 0
    day = 0

    for j in num:
        lst.append(j)
    year = int(lst[0])*1000 + int(lst[1])*100 + int(lst[2])*10 + int(lst[3])
    month = int(lst[4])*10 + int(lst[5])
    day = int(lst[6])*10 + int(lst[7])


    if year <= 0:
        print(f'#{i} -1')
    elif month > 12 or month == 0:
        print(f'#{i} -1')
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if day > 31 or day == 0:
            print(f'#{i} -1')
        else:
            print(f'#{i} {lst[0]}{lst[1]}{lst[2]}{lst[3]}/{lst[4]}{lst[5]}/{lst[6]}{lst[7]}')
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day > 30 or day == 0:
            print(f'#{i} -1')
        else:
            print(f'#{i} {lst[0]}{lst[1]}{lst[2]}{lst[3]}/{lst[4]}{lst[5]}/{lst[6]}{lst[7]}')
    elif month == 2:
        if day > 28 or day == 0:
            print(f'#{i} -1')
        else:
            print(f'#{i} {lst[0]}{lst[1]}{lst[2]}{lst[3]}/{lst[4]}{lst[5]}/{lst[6]}{lst[7]}')
    else:
        print(f
T = int(input())
thirty = [4, 6, 9, 11]
thirty_1 = [1, 3, 5, 7, 8, 10, 12]

for t in range(1, T+1):
    s = input()
    year = s[:4]
    month = s[4:6]
    day = s[-2:]

    if int(year) > -1:
        if (int(month) in thirty) and (0 < int(day) < 31):
            print(f'#{t} '+year+'/'+month+'/'+day)
        elif (int(month) in thirty_1) and (0 < int(day) < 32):
            print(f'#{t} '+year+'/'+month+'/'+day)
        elif (month == '02') and (0 < int(day) < 29):
            print(f'#{t} '+year+'/02/'+day)
        else:
            print(f'#{t} -1')
    else:
        print(f'#{t} -1')
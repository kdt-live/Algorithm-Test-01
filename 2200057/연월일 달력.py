T = int(input())

month_31 = ['01', '03', '05', '07', '08', '10', '12']
month_30 = ['04', '06', '09', '11']

for t in range(1, T+1):
    date = input()
    y, m, d = date[:4], date[4:6], date[6:]
    if int(m) < 1 or int(m) > 12 or int(d) < 1 or int(d) > 31:
        print(f'#{t} -1')
    elif m in month_30 and int(d) > 30:
        print(f'#{t} -1')
    elif m == '02' and int(d) > 28:
        print(f'#{t} -1')
    else:
        print(f'#{t} {y}/{m}/{d}')
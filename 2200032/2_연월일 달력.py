# 2 (2056. 연월일 달력)
T = int(input())
days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
for test_case in range(1, T+1):
    N = str(input())
    res = ''
    slash = '/'
    year = N[0:4]
    month = N[4:6]
    day = N[6:8]
    if 0 < int(month) < 13 and 0< int(day) <= days[int(month)]:
        res = year + slash + month + slash + day
    else:
        res = '-1'
    print(f'#{test_case} {res}')
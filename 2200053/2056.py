# 연월일 달력
# 딕셔너리 사용???
#m_d = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
T = int(input())
for t in range(1, T+1):
    n = input()
    year = n[0:4]
    month = n[4:6]
    day = n[6:8]

    if month == '00' or month > '12':
        print(f'#{t} -1')
    else:
        # print('1')
        if month == '02':
            #print('1')
            if day > '28':
                print(f'#{t} -1')
            else:
                print(f'#{t} {year}/{month}/{day}')
        else:
            print(f'#{t} {year}/{month}/{day}')
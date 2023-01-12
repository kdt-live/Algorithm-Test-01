T = int(input())

for i in range(T):
    ipt = input()
    flag = 0
    month = int(ipt[4:6])
    day = int(ipt[6:])

    if month not in range(1, 13):
        flag = 1
    elif (month in (1, 3, 5, 7, 8, 10, 12)) * (day not in range(1, 32)):
        flag = 1
    elif (month in (4, 6, 9, 11)) * (day not in range(1, 31)):
        flag = 1
    elif (month == 2) * (day not in range(1, 29)):
        flag = 1

    if flag == 1:
        print(f'#{i + 1} -1')
    else:
        print(f'#{i + 1} {ipt[0:4]}/{ipt[4:6]}/{ipt[6:]}')
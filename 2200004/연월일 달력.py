t = int(input())
day31 = [1, 3, 5, 7, 8, 10, 12]
day30 = [4, 6, 9, 11]
day28 = [2]

for i in range(1, t+1):
    date = input()
    if int(date[4:6]) in day31:
        if int(date[6:]) <= 31:
            print(f'#{i} {date[0:4]}/{date[4:6]}/{date[6:]}')
        else:
            print(f'#{i}', -1)

    elif int(date[4:6]) in day30:
        if int(date[6:]) <= 30:
            print(f'#{i} {date[0:4]}/{date[4:6]}/{date[6:]}')
        else:
            print(f'#{i}', -1)

    elif int(date[4:6]) in day28:
        if int(date[6:]) <= 28:
            print(f'#{i} {date[0:4]}/{date[4:6]}/{date[6:]}')
        else:
            print(f'#{i}', -1)

    else:
        print(f'#{i}', -1)


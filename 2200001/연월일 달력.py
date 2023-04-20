# 연월일 달력
T = int(input())

for t in range(1, T+1):
    date = input()
    year = int(date[:4])
    mon = int(date[4:6])
    day = int(date[6:8])

    if mon < 1 or mon > 12:
        print(f"#{t} -1")
        continue

    if mon in [1, 3, 5, 7, 8, 10, 12]:
        if day > 31 or day < 1:
            print(f"#{t} -1")
            continue

    if mon in [4, 6, 9, 11]:
        if day > 30 or day < 1:
            print(f"#{t} -1")
            continue

    if mon in [2]:
        if day >28 or day < 1:
            print(f"#{t} -1")
            continue

    print(f"#{t} %04d/%02d/%02d" %(year,mon,day))
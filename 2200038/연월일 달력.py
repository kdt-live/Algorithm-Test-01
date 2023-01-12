T = int(input())
for test_case in range(1, T + 1):
    N = str(input())
    # 그림 1
    year = N[0:4]
    month = N[4:6]
    day = N[6:]
    fail = -1
    # 표 1 해결 못함

    if 0 < int(month) < 13 and 0 < int(day) < 29:
        print("#{}/{}/{}/{}".format(test_case,year,month,day))
    else:
        print("#{} {}".format(test_case,fail))

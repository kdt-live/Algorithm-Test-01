month_31 = [1, 3, 5, 7, 8, 10, 12]
month_30 = [4, 6, 9, 11]
i_t = int(input())
for i_1 in range(i_t):
    s_date = input()
    s_yr = s_date[:4]
    s_mth = s_date[4:6]
    i_mth = int(s_mth)
    s_dy = s_date[6:]
    i_dy = int(s_dy)
    if i_mth in month_31:
        if i_dy <= 31:
            print(f'#{i_1 + 1} {s_yr}/{s_mth}/{s_dy}')
        else:
            print(f'#{i_1 +1} -1')
    elif i_mth in month_30:
        if i_dy <= 30:
            print(f'#{i_1 + 1} {s_yr}/{s_mth}/{s_dy}')
        else:
            print(f'#{i_1 +1} -1')
    elif i_mth == 2:
        if i_dy <= 28:
            print(f'#{i_1 + 1} {s_yr}/{s_mth}/{s_dy}')
        else:
            print(f'#{i_1 +1} -1')
    else:
        print(f'#{i_1 +1} -1')
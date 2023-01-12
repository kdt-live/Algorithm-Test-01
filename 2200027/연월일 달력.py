case = int(input())
special_month = [2, 9, 11, 4, 6]

for i in range(1, case+1):
    nums = input() # 
    year = nums[:4]
    month = int(nums[4:6])
    day = int(nums[6:])

    if (month > 12 or month < 1) or (day > 31 or day < 1): # 날짜형식에 맞지 않음.
        print(f'#{i} -1')
    elif month in special_month: # 28일, 30일까지 있는 달
        if month == 2 and day < 29:
            print(f'#{i} {year}/{nums[4:6]}/{nums[6:]}')
        elif month != 2 and day < 31:
            print(f'#{i} {year}/{nums[4:6]}/{nums[6:]}')
        else:
            print(f'#{i} -1')
    else:
        print(f'#{i} {year}/{nums[4:6]}/{nums[6:]}')

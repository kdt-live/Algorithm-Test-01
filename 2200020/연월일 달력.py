T = int(input())

date_dict = {'01':'31', '02':'28', '03':'31', '04':'30', '05':'31', '06':'30', '07':'31', '08':'31', '09':'30', '10':'31', '11':'30', '12':'31'}

for test_case in range(1, T + 1):
    date = str(input())
    year = date[0:4]
    month = date[4:6]
    day = date[6:]
    fail_answer = ''
    if (month not in date_dict) or (int(day) > int(date_dict[month])) or (int(day) <= 0):
        fail_answer = '-1'
    
    if fail_answer == '-1':
        print(f'#{test_case} {fail_answer}')
    else:
        print(f'#{test_case} {year}/{month}/{day}')

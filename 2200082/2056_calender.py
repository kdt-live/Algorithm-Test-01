import sys
sys.stdin = open('EXAM-01/2200082/input.txt', 'r')

import datetime

T = int(input())
for t in range(1, T+1):
    test_input = input()
    y_part = test_input[:4]
    m_part = test_input[4:6]
    d_part = test_input[-2:]

    result = ''

    if int(m_part) in [1, 3, 5, 7, 8, 10, 12]:
        if int(d_part) in range(1, 32):
            result = str(y_part + '/' + m_part + '/' + d_part)
    
    elif int(m_part) in [4, 6, 9, 11]:
        if int(d_part) in range(1, 31):
            result = str(y_part + '/' + m_part + '/' + d_part)
    elif int(m_part) == 2:
        if int(d_part) in range(1, 29):
            result = str(y_part + '/' + m_part + '/' + d_part)
        else:
            result = -1
    else:
        result = -1

    print(f'#{t} {result}')




    # if str(f'{m_part}/{d_part}') == '02/28':
    #     print(f'#{t} {y_part}/{m_part}/{d_part}')
    
    # else:
    #     try:
    #         date_info = datetime.date(year=int(y_part), month=int(m_part), day=int(d_part))
    #         if str(datetime.date.strftime(date_info, '%m/%d')) == '02/29':
    #             print(f'#{t} -1')
    #         else:
    #             the_day = datetime.date.strftime(date_info, '%Y/%m/%d')
    #             print(f'#{t} {the_day}')
    #     except:
    #         print(f'#{t} -1')
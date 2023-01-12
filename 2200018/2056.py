# 연월일 달력
import sys, datetime

sys.stdin = open('input_2056.txt')

T = int(input())
d = [31,28,31,30,31,30,31,31,30,31,30,31]

for i in range(T):
    s = input()
    
    year = s[:4]
    month = s[4:6]
    day = s[6:]

    # print(year, month, day)
    
    if int(month) in range(1, 13):
        # print(int(month))
        # print(d[int(month)-1])
        if int(day) in range(1, d[int(month)-1]+1):
            print(f'#{i+1} {year}/{month}/{day}')
        else:
            print(f'#{i+1} -1')
    else:
        print(f'#{i+1} -1') 

    # if int(s[6:]) in range(1, d[int(s[4:6])+1]):
    #     print(s)
    #     # print(f'#{i+1} {s[:4]}/{s[4:6]}/{s[6:]}')
    # else:
    #     print(f'#{i+1} -1')

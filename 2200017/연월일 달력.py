# 2056. 연월일 달력
T = int(input())
days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
for test_case in range(1, T + 1):
    n = input()
    y = n[0:4]
    m = n[4:6]
    d = n[6:8]
   
    sum = ''
    if 0 < int(m) < 13 and 0 < int(d) <= days[int(m)]:
        sum = y + '/' + m + '/' + d
    else:
        sum += '-1'

    print(f'#{test_case} {sum}')
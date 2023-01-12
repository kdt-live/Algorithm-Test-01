# 2056. 연월일 달력
# 연월일 순으로 구성된 8자리의 날짜가 입력으로 주어진다.
# 날짜가 유효하면 YYYY/MM/DD 형식으로 출력
# 유효하지 않을경우 -1

T = int(input())

for i in range(1,T+1):
    num = input()
    if int(num[4:6]) == 2:
        if int(num[6:8]) <=28:
            print(f'#{i} {num[0:4]}/{num[4:6]}/{num[6:8]}')
        else:
            print(f'#{i} -1')
    if int(num[4:6]) == 1 or int(num[4:6]) == 3 or int(num[4:6]) == 5 or int(num[4:6]) == 7 or int(num[4:6]) == 8 or int(num[4:6]) == 10 or int(num[4:6]) == 12:
        if int(num[6:8]) <=31:
            print(f'#{i} {num[0:4]}/{num[4:6]}/{num[6:8]}')
        else:
            print(f'#{i} -1')
    if int(num[4:6]) == 4 or int(num[4:6]) == 6 or int(num[4:6]) == 9 or int(num[4:6]) == 11:
        if int(num[6:8]) <=30:
            print(f'#{i} {num[0:4]}/{num[4:6]}/{num[6:8]}')
        else:
            print(f'#{i} -1')
    if int(num[4:6]) < 1 or int(num[4:6]) > 12:
        print(f'#{i} -1')
# 연월일 달력
# 연월일 순으로 구성된 8자리의 날짜가 입력으로 주어진다.
# 해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면
#  ”YYYY/MM/DD”형식으로 출력하고,
# 날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라.
# 연월일로 구성된 입력에서 월은 1~12 사이 값을 가져야 하며
# 일은 [표1] 과 같이, 1일 ~ 각각의 달에 해당하는 날짜까지의 값을 가질 수 있다.
# 입력
# 5
# 22220228
# 20150002
# 01010101
# 20140230
# 11111111 

month1 = [1, 3, 5, 7, 8, 10, 12]
month2 = [4, 6, 9, 11]
T = int(input())
for t in range(1, T+1):
    num = input()
    year = num[0:4]
    month = num[4:6]
    day = num[6:8]
    if month in month1:
        if 1 <= day <= 31:
            print(f'#{t} {year}/{month}/{day}')
        else:
            print('-1')
    elif month in month2:
        if 1 <= day <= 30:
            print(f'#{t} {year}/{month}/{day}')
        else:
            print('-1')
    elif month == 2:
        if 1 <= day <= 28:
            print(f'#{t} {year}/{month}/{day}')
        else:
            print('-1')

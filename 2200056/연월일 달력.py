# 연월일 순으로 달력 프린트 / 날짜가 유호하지 않으면 -1 출력
T = int(input())

for t in range(1, T + 1):
    day_numbers = input() # 요소 하나하나 나누기 위해서 글자로 받기

    month = int(day_numbers[4:6]) # 필요한 변수 만들기
    day = int(day_numbers[6:8]) # 필요한 변수 만들기

    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 11: # 31일
        if 0 < day < 32:
            print("#{0} {1}/{2}/{3}".format(t, day_numbers[0:4], day_numbers[4:6], day_numbers[6:8]))
        else:
            print("#{0} -1".format(t))

    elif month == 4 or month == 6 or month == 9 or month == 11: # 30일
        if 0 < day < 31:
            print("#{0} {1}/{2}/{3}".format(t, day_numbers[0:4], day_numbers[4:6], day_numbers[6:8]))
        else:
            print("#{0} -1".format(t))

    elif month == 2: # 28일
        if 0 < day < 29:
            print("#{0} {1}/{2}/{3}".format(t, day_numbers[0:4], day_numbers[4:6], day_numbers[6:8]))
        else:
            print("#{0} -1".format(t))
    else:
        print("#{0} -1".format(t))


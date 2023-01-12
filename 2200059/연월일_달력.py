# 2. 연월일달력

T = int(input())
for test_case in range(1, T + 1):
    nums = input()

    a = nums[-len(nums):-4]
    b = nums[-4:-2]
    c = nums[-2:]

    년 = int(nums[-len(nums):-4])
    월 = int(nums[-4:-2])
    일 = int(nums[-2:])

    if 년 < 1000:
        print(a, '/', 월, '/', 일, sep='')
    elif 월 == 2 and 일 < 29:
        print(년, '/', 월, '/', 일, sep='')
    elif 월 == 1 and 일 < 32:
        print(년, '/', 월, '/', 일, sep='')
    elif 월 == 3 and 일 < 32:
        print(년, '/', 월, '/', 일, sep='')
    elif 월 == 5 and 일 < 32:
        print(년, '/', 월, '/', 일, sep='')
    elif 월 == 7 and 일 < 32:
        print(년, '/', 월, '/', 일, sep='')
    elif 월 == 8 and 일 < 32:
        print(년, '/', 월, '/', 일, sep='')
    elif 월 == 10 and 일 < 32:
        print(년, '/', 월, '/', 일, sep='')
    elif 월 == 12 and 일 < 32:
        print(년, '/', 월, '/', 일, sep='')
    elif 월 == 4 and 일 < 31:
        print(년, '/', 월, '/', 일, sep='')
    elif 월 == 6 and 일 < 31:
        print(년, '/', 월, '/', 일, sep='')
    elif 월 == 9 and 일 < 31:
        print(년, '/', 월, '/', 일, sep='')
    elif 월 == 11 and 일 < 31:
        print(년, '/', 월, '/', 일, sep='')

    else:
        print(-1)

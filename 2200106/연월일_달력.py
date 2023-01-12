def is_month(m, d):
    if m in range(1, 13):
        return(is_day(m, d))
    else:
        return False

def is_day(m, d):
    if d <= 0:
        return False
    if m <= 8:
        if m % 2 == 1 and d <= 31:
            return True
        if m == 2 and d <= 28:
            return True
        elif m % 2 == 0 and d <= 30:
            if m == 2 and d >28:
                return False
            else:
                return True
        else:
            return False
    if m <= 12:
        if m % 2 == 0 and d <= 31:
            return True
        elif m % 2 == 1 and d <= 30:
            return True
        else:
            return False     

T = int(input())
for test_case in range(1, T + 1):
    date = input()
    y = date[:4]
    m = date[4:6]
    d = date[6:]
    if is_month(int(m), int(d)):
        print(f'#{test_case} {y}/{m}/{d}')
    else:
        print(f'#{test_case} -1')
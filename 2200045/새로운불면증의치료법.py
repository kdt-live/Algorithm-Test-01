# 1288
T = int(input())

for t in range(1, T+1):
    number = int(input())
    num = number
    numbers_dict = {}
    a = 0
    while len(numbers_dict) < 10:
        num = str(num)
        for n in num:
            numbers_dict[n] = 0
        num = int(num)
        num += number
        a += 1
    print(f'#{t} {a*number}')

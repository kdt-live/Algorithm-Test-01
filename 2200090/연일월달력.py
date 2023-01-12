# T = int(input())

# for t in range(1, T+1):
#     a = input()
#     year = int(a[0:4])
#     month = int(a[4:6])
#     day = int(a[6:8])
#     list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     b = '-1'
#     if month <= 12 and 1 <=month and 1 <= day and day <=list[month-1]:
#         b = a[0:4]+"/"+a[4:6]+"/"+a[6:8]
#     print(f'#{t} {b}')
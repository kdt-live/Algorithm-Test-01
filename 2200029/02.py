# import sys
# sys.stdin = open("input (2).txt", "r")

num = input()
month = num[5:7]
day = num[8:]
i = 0
j = 0

form = []
while i < 8:
    if j == 4 or j == 7:
        form.append("/")
        i -= 1
    else:
        form.append(num[i])
    j += 1
    i += 1


if month == '01' or month == '03' or month == '05' or month == '07' or month == '10' or month == '12':
    if int(day) not in range(1,32):
        print("-1")
elif month == '04' or month == '06' or month == '09' or month == '11':
    if int(day) not in range(1, 31):
        print("-1")
elif month == '02':
    if int(day) not in range(1,29):
        print("-1")
else:
    for text in form:
        print(text,end="")


    # form = []
    # while i < 8:
    #     if j == 4 or j == 7:
    #         form.append("/")
    #         i -= 1
    #     else:
    #         form.append(num[i])
    #     j += 1
    #     i += 1

    # for text in form:
    #     print(text,end="")



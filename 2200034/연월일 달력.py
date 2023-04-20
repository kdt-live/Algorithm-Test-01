T = int(input())
for i in range(1, T + 1):
    dl = input()

    year = dl[:4]
    month = dl[4:6]
    day = dl[6:]

    if int(month) > 12 or int(month) <= 0 or int(day) > 31 or int(day) <= 0:
        print(f'#{i}',-1)

    elif int(month) == 2 and int(day) > 28:
        print(f'#{i}',-1)
    

    else:
        print(f'#{i}' +" " + year,month,day,sep="/" )
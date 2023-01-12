T=int(input())

for t in range (1, T+1) :
    N = input()
    year = int(N[0:4])
    mon = int(N[4:6])
    day = int(N[6:8])

    if mon > 12 or mon < 1 :
        print(f"#{t} -1")    
        continue

    if mon == 1 or mon == 3 or mon == 5 or mon == 7 or mon == 8 or mon == 10 or mon == 12 :
        if 1 <= day <= 31 :
            print(f"#{t} {year:04d}/{mon:02d}/{day:02d}")
        else :
            print(f"#{t} -1")
            continue

    if mon == 2 :
        if 1<= day <= 28 :
            print(f"#{t} {year:04d}/{mon:02d}/{day:02d}")
        else :
                print(f"#{t} -1")
                continue
            
    if mon == 4 or mon == 6 or mon == 9 or mon == 11 :
        if 1<= day <= 30 :
            print(f"#{t} {year:04d}/{mon:02d}/{day:02d}")
        else :
            print(f"#{t} -1")
            continue
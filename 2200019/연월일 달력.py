n = int(input())

for i in range(1,n+1):
    day = str(input())
    if len(day) == 8:
        if 101 <= int(day[4:8]) <= 131: 
            print(f'#{i} {day[0:4]}/{day[4:6]}/{day[6:8]}')
        elif 201 <= int(day[4:8]) <= 228: 
            print(f'#{i} {day[0:4]}/{day[4:6]}/{day[6:8]}')
        elif 301 <= int(day[4:8]) <= 331:
            print(f'#{i} {day[0:4]}/{day[4:6]}/{day[6:8]}')
        elif 401 <= int(day[4:8]) <= 430:
            print(f'#{i} {day[0:4]}/{day[4:6]}/{day[6:8]}')
        elif 501 <= int(day[4:8]) <= 531:
            print(f'#{i} {day[0:4]}/{day[4:6]}/{day[6:8]}')
        elif 601 <= int(day[4:8]) <= 630:
            print(f'#{i} {day[0:4]}/{day[4:6]}/{day[6:8]}') 
        elif 701 <= int(day[4:8]) <= 731:
            print(f'#{i} {day[0:4]}/{day[4:6]}/{day[6:8]}') 
        elif 801 <= int(day[4:8]) <= 831:
            print(f'#{i} {day[0:4]}/{day[4:6]}/{day[6:8]}') 
        elif 901 <= int(day[4:8]) <= 930:
            print(f'#{i} {day[0:4]}/{day[4:6]}/{day[6:8]}') 
        elif 1001 <= int(day[4:8]) <= 1031:
            print(f'#{i} {day[0:4]}/{day[4:6]}/{day[6:8]}') 
        elif 1101 <= int(day[4:8]) <= 1130:
            print(f'#{i} {day[0:4]}/{day[4:6]}/{day[6:8]}') 
        elif 1201 <= int(day[4:8]) <= 1231:
            print(f'#{i} {day[0:4]}/{day[4:6]}/{day[6:8]}') 
        else:
            print(f'#{i} -1')
    else:
        print(f'#{i} -1')        
             
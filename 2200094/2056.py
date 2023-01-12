




T = int(input())

for ele in range(1, T + 1):


    date = str(input())

    year = date[0:4]
    month = date[4:6]
    day = date[6:8]

    list = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 
            9:30, 10:31, 11:30, 12:31}



    if 0 < month < 13 and day <= list[month]:
        print(f'#{ele} {year}/{month}/{day}')
    
    else:
        print(f'#{ele}' -1)

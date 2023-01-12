T= int(input())
for i in range(1, T+1) :
    x = input()
    for j in x :
        # 프린트용 
        year_s = x[0] +  x[1] +  x[2] +  x[3]
        month_s = x[4] +  x[5]
        date_s = x[6] +  x[7]
        
        # 계산용
        year = int(x[0] +  x[1] +  x[2] +  x[3]) 
        month = int(x[4] +  x[5])
        date =  int(x[6] +  x[7])
    if year < 1 :
        print(f"#{i} -1")
    else :
        if month >= 1 and month <= 12 :
            if month == 2 :
                if date >= 1 and date <=28 :
                    print(f"#{i} {year_s}/{month_s}/{date_s}")
                else :
                    print(f"#{i} -1")
            if month == 1 or month ==3 or month ==5 or month ==7 or month == 8 or month == 10 or month == 12:
                if date >= 1 and date <=31 :
                    print(f"#{i} {year_s}/{month_s}/{date_s}")
                else :
                    print(f"#{i} -1")
            if month == 4 or month ==6 or month ==9 or month == 11:
                if date >= 1 and date <=31 :
                    print(f"#{i} {year_s}/{month_s}/{date_s}")
                else :
                    print(f"#{i} -1")                   
        else :
            print(f"#{i} -1")
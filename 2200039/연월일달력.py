T = int(input()); year_month_day = []; answer = []
for i in range(T): year_month_day.append(input())
for i in range(len(year_month_day)):
    year = int(year_month_day[i][:4]); month = int(year_month_day[i][4:6]); day = int(year_month_day[i][6:])
    if year > 0 and 0 < month <= 12:
        if month in [1,3,5,7,8,10,12]:
            if 1 <= day <= 31: answer.append("{}/{}/{}".format(year_month_day[i][:4],year_month_day[i][4:6],year_month_day[i][6:]))
            else: answer.append("-1")
        elif month in [4,6,9,11]:
            if 1 <= day <= 30: answer.append("{}/{}/{}".format(year_month_day[i][:4],year_month_day[i][4:6],year_month_day[i][6:]))
            else: answer.append("-1")
        elif month == 2:
            if 1 <= day <= 28: answer.append("{}/{}/{}".format(year_month_day[i][:4],year_month_day[i][4:6],year_month_day[i][6:]))
            else: answer.append("-1")
    else: answer.append("-1")
for i in range(len(answer)): print("#{} {}".format(i+1, answer[i]))
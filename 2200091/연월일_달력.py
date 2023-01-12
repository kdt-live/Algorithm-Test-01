test = int(input())

for i in range(test):
    date = input()
    year = date[:4]

    if 0 < int(date[4:6]) < 13:
        month = date[4:6]
    else:
        print(f"#{i+1} -1")
        continue

    if month in ["01", "03", "05", "07", "08", "10", "12"]:
        if 0 < int(date[6:]) < 32:
            day = date[6:]
        else:
            print(f"#{i+1} -1")
            continue
    elif month in ["04", "06", "09", "11"]:
        if 0 < int(date[6:]) < 31:
            day = date[6:]
        else:
            print(f"#{i+1} -1")
            continue    
    elif month == "02":
        if 0 < int(date[6:]) < 29:
            day = date[6:]
        else:
            print(f"#{i+1} -1")
            continue    

    print(f"#{i+1} {year}/{month}/{day}")
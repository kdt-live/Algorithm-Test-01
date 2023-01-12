T = int(input())
for i in range(1, T+1) :
    x =int(input())
    x_s = str(x)
    cnt = 1
    dict_x = {}
    for j in x_s :
        if j != dict_x:
            dict_x[j] = 1
        else :
            continue
    while True :
        if "0" in dict_x and "1" in dict_x and "2" in dict_x and "3" in dict_x and "4" in dict_x and "5" in dict_x and "6" in dict_x and "7" in dict_x and "8" in dict_x and "9"  in dict_x :
            break   
        else :
            cnt +=1
            result = x * cnt
            x_s = str(result)
            for j in x_s :
                if j != dict_x:
                    dict_x[j] = 1
                else :
                    continue
    print(f"#{i} {result}")        
T = int(input())

for i in range(1, T+1) :
    num = int(input())
    num_list = [0]*10
    sum = 0

    while(True) :
        if 0 not in num_list :
            break
        else :
            sum += 1
            number = str(num*sum)
            for j in range(len(number)) :
                num_list[int(number[j])] = 1
                
    print(f"#{i} {number}")
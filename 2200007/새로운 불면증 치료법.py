T = int(input())

for t in range(1, T+1) :
    N = int(input())
    list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    k = 0

    while(True) :
        if 0 not in list :
            break
        else :
            k += 1
            num = str(N*k)
            for j in range(len(num)) :
                list[int(num[j])] = 1

    print(f"#{t} {num}")
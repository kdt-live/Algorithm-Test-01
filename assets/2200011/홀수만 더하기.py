T = int(input())
for i in range(1, T+1) :
    x = list(map(int, input().split()))
    cnt = 0
    for j in x :
    	if j % 2 != 0 :
            cnt +=j
        else :
            continue
    print(f"#{i} {cnt}")
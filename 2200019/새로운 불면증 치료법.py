n= int(input())


for i in range(1,n+1):
    N = int(input())
    K = N
    N_list = []
    for j in str(N):
        if j not in N_list:
            N_list.append(j)
    while len(N_list) < 10:
        N += K
        for q in str(N):
            if q not in N_list:
                N_list.append(q)
                
    print(f'#{i} {N}')
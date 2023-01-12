n = int(input())


for i in range(1,n+1):
    odd_list = (list(map(int,input().split())))
    cnt = 0
    for j in odd_list:
        if j % 2 == 1:
            cnt += j
    print(f'#{i} {cnt}',sep='')        
            
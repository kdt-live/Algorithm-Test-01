T=int(input())
for i in range(1,T+1):
    x=list(map(int,input().split()))
    s=0
    for k in x:
        if k%2 !=0:
            s+=k
    print(f'#{i} {s}')
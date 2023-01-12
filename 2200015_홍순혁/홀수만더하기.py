a = int(input())

for i in range(1,a+1):
    N = list(map(int,input().split()))
    b = 0
    for e in N:
        if e % 2 ==1:
            b += e
            
    print(f'#{i} {b}')
    
        

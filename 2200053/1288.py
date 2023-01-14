# 새로운 불면증 치료법

T = int(input())
for t in range(1, T+1):
    N = int(input())
    num = []
    cnt = 0
    N_num = N
    
    while(len(num) != 10):
        cnt += 1
        N_num = N * cnt  
        
        for i in str(N_num):
            if i in num:
                continue
            else:
                num.append(i)
                num.sort()
               
    print(f"#{t} {N*cnt}")
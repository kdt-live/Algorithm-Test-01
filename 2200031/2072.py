T = int(input())

for i in range(1, T+1):
    num = list(map(int, input().split()))
    sum = 0
    
    for j in num:
        if j%2 != 0:
            sum += j
            
    print(f"#{i} {sum}")
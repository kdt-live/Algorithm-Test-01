T = int(input()) 

for t in range(1, T+1):
    num = list(map(int,input().split())) 
    result = 0
    for i in num:
        if i % 2 == 1:
            result += i
    print(f'#{t} {result}')
        
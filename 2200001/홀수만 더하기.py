# 홀수만 더하기
T = int(input())

for t in range(1, T+1):
    cnt = 0 
    numbers = list(map(int, input().split()))
    for i in numbers:
        if i % 2 == 1:
            cnt += i
            
print(f"#{t} {cnt}")
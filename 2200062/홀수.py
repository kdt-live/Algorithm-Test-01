# 홀수만 더하기

T = int(input()) 

for t in range(1, T+1):
    numbers = list(map(int,input().split()))
    sum = 0

    for a in numbers:
        if a%2 == 1:
             sum += a
    print(f"# {t} {sum}")
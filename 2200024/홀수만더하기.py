# 홀수만 더하기
T = int(input())

for t in range(1, T+1) :

    li = list(map(int, input().split()))
    summ = 0

    for i in li :
        if (i % 2 != 0) :
            summ += i
    print(f"#{t} {summ}") 

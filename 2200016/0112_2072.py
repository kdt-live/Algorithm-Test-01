# 2072. 홀수만 더하기
# 10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력

T = int(input())
for i in range(1,T+1):
    n= 0
    number = list(map(int,input().split()))
    for m in number:
        if m%2 == 1:
            n = n + m
    print(f'#{i} {n}')    



# 2072. 홀수만 더하기
import sys
sys.stdin = open("input.txt", "r")

T=int(input())
for tc in range(T):
    numbers=list(map(int,input().split()))
    sum=0
    for e in numbers:
        if e%2==0:
            continue
        else:
            sum+=e
    print(f'#{tc+1} {sum}')
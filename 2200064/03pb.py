# 정수 N의 약수를 오름차순으로 출력

N = int(input())

for i in range(1, N+1):
    if N % i == 0:
        print(i, end=' ')
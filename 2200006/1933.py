# 1933 .간단한 N 의 약수
N = int(input())

for i in range(1, N + 1):
    if N % i == 0:
        print(i, end = ' ')
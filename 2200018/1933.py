# 간단한 N의 약수
n = int(input())

for i in range(n):
    if n % (i + 1) == 0:
        print(i + 1, end=' ')

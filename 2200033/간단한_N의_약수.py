# 1933 .간단한 N 의 약수
N = int(input())
lst = []

for i in range(1, N+1):
    if N % i == 0:
        lst.append(i)

print(*lst)
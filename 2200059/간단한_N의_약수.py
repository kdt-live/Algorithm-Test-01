# 4. 간단한 N의 약수

N = int(input())
result = []
for i in range(1, N+1):
    if N % i == 0:
        result.append(i)

print(*result)

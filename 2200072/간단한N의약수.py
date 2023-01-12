# 1933 간단한 N의 약수

n = int(input())

result = []
for num in range(1,n+1):
  if n%num == 0:
    result.append(num)
print(*result)
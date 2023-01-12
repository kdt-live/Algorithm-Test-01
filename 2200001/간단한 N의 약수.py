# 간단한 N의 약수
numbers = int(input())
n_list = []

for i in range(1, numbers+1):
    if numbers % i == 0:
        n_list.append(i)

print(*n_list)
# 1
n = int(input())
div_n = []

for i in range(1, n+1):
    if n % i == 0:
        div_n.append(str(i))
print(' '.join(div_n))



# 2
n = int(input())

for i in range(1, n+1):
    if n % i == 0:
        print(i, end=' ')
a = int(input())
yaksoo = [i for i in range(1, a+1) if a % i == 0]
for i in yaksoo:
    print(i, end=' ')
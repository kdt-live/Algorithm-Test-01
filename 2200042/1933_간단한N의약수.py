# 1933_간단한N의약수.py
n = int(input())
for i in range(1,n+1,1):
    if n%i == 0:
        print(i)

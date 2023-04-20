N = int(input())

# N % n == 0 일때 n은 N의 약수

for i in range(1,N+1):
    if N % i == 0:
        print(i, end = ' ')
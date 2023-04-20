N = int(input())
1 <= N <= 1000

for n in range (1,N+1):
    if N%n ==0 :
        print(n, end = ' ')
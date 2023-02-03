N = 10 #int(input())
n = []
for i in range(1,N + 1):
    if 1 <= N <= 100: 
        if N % i == 0:
            n.append(i)

print(*sorted(n))
N = int(input())
for i in range(1, N + 1):
    if N%2 == 0:
        N = i * i
        print(N, end=" ")

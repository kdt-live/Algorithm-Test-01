# 문제풀이 코드
n = int(input())
I = []
for N in range(1, n+1):
    if n % N == 0:
        I.append(N)
print(*I)
N = int(input())
nums = []

for n in range(1, N+1):
    if N % n == 0:
        nums.append(n)

print(*nums)
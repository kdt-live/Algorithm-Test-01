N = int(input())
result = [num for num in range(1, N+1) if N % num == 0]
print(*result)
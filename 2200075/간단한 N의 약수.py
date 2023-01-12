N = int(input())
numbers = []
for index in range(1, N+1):
    if 0 == (N % index):
        numbers.append(index)
print(*numbers)
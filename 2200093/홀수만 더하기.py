T = int(input())

for i in range(T):
    numbers = list(map(int, input().split()))
    new_numbers = []

    for j in range(10):
        if numbers[j] % 2 == 1:
            new_numbers.append(numbers[j])
    print(f'#{i+1} {sum(new_numbers)}')
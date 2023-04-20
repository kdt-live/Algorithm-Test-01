# 못 품

T = int(input())

for i in range(T):
    N = int(input())

    cnt = 1
    numbers = []

    while True:
        numbers.append(list(str(cnt * N)))
        numbers = list(set(numbers))
        if len(numbers) == 10:
            break
        cnt += 1
    print(f'#{i+1} {cnt*N}')
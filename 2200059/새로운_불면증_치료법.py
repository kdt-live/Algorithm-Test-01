# 5. 새로운 불면증 치료법
T = int(input())
for x in range(1, T + 1):
    N = int(input())
    limit = []
    k = 1
    while True:
        n = k*N
        for a in list(str(n)):
            if a not in limit:
                limit.append(a)
        if len(limit) == 10:
            break
        k += 1

    print(f'#{x} {n}')

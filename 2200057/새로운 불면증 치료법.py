T = int(input())
result = set(x for x in range(10))
for t in range(1, T+1):
    origin_n = int(input())
    n = 0
    num = set()
    while num != result:
        n += origin_n
        li = str(n)
        for l in li:
            num.add(int(l))
    print(f'#{t} {n}')
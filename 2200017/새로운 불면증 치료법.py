#1288. 새로운 불면증 치료법
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    s = set()
    c = 1
    while True:
        for j in str(n):
            s.add(j)
        if len(s) == 10:
            break
        n //= c
        c += 1
        n *= c
    
    print(f'#{test_case} {n}')
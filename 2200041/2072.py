# 문제풀이 코드
t = int(input())
for T in range(1, t+1):
    ns = list(map(int, input().split()))
    A = 0
    for Ns in ns:
        if Ns % 2 == 1:
            A += Ns
        else:
            continue
    print(f'#{T} {A}')
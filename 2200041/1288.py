# 문제풀이 코드
t = int(input())
for T in range(1, t+1):
    s = int(input())
    n = []
    a = 0
    while len(n) < 10:      # 갯수 10보다 작으면 계속 돌려
        a += s
        for A in str(a):
            if A not in n:
                n.append(A)
    print(f'#{T} {a}')
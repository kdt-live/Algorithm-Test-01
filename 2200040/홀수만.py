T = int(input())

for t in range(1, T+1):
    N = list(map(int, input().split()))
    con = 0
    for i in N:
        if i%2 == 1:
            con += i
    print(f"#{t} {con}")
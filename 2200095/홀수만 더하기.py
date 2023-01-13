T = int(input())

for t in range(1, T + 1):
    input_ = list(map(int, input().split()))
    res = 0
    for i in input_:
        if i % 2 == 1:
            res += i
    print(f"#{t} {res}")
        


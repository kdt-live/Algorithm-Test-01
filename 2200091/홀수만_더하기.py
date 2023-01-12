test = int(input())

for i in range(test):
    numbers = list(map(int, input().split()))
    ans = 0
    for j in numbers:
        if j % 2 != 0:
            ans += j

    print(f"#{i+1} {ans}")
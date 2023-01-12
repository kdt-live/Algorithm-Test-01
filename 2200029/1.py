import sys
sys.stdin = open("input (2).txt", "r")

T = int(input())

for t in range(1, T + 1):
    num = list(map(int, input().split()))
    total = 0
    for i in num:
        if i % 2 == 1:
            total += i
    print(f"#{t} {total}")

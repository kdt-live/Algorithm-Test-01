# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    n = input()
    if n[5]=='0' or n[-2]=='3':
        print(f"#{t} -1")
    else:
        print(f"#{t} {n[:4]}/{n[4:6]}/{n[6:]}")
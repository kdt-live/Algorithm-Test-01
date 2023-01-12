# import sys
# sys.stdin = open("input.txt", "r")


a = int(input())
for i in range(a):
    sum = 0
    l = list(map(int,input().split()))
    for j in l:
        if j%2 == 1:
            sum +=j
    print(f'#{i+1} {sum}')

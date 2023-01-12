# import sys
# sys.stdin = open("input.txt", "r")

a = int(input())
for i in range(a):
    b = int(input())
    l = []
    n = 1
    while True:

        k = str(b*n)
        for j in k:
            l.append(j)
        n +=1
        if len(set(l)) == 10:
            break

    print(f'#{i+1} {b*(n-1)}')

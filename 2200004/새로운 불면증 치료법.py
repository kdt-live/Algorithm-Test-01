t = int(input())

b = set()
for i in range(10):
    b.add(f'{i}')
#######################

for i in range(1, t+1):
    n = int(input())
    a = set()
    cnt = 0
    while a != b:
        cnt += 1
        for j in str(cnt*n):
            a.add(j)
    print(f'#{i}', cnt*n)

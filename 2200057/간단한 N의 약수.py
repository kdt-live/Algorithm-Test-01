n = int(input())
li = set()
for i in range(1, int(n**1/2)+1):
    if n % i == 0:
        li.add(i)
        if i != (n//i):
            li.add(n//i)
for i in sorted(li):
    print(i, end=' ')
# 새로운 불면증 치료법
import sys

sys.stdin = open('input_1288.txt')


T = int(input())

for i in range(T):
    s = set()
    n = int(input())
    s.update(*str(n))

    k = 1
    while len(s) < 10:
        k += 1
        t = n * k
        s.update(*str(t))
    
    print(f'#{i + 1} {t}')

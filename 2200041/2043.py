# 문제풀이 코드
P, K = map(int, input().split())
c = 1
while K < P:
    K += 1
    c += 1
print(c)
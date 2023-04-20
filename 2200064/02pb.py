# 비밀번호

p, k = map(int, input().split())

if p >= k:
    print(p - k + 1)
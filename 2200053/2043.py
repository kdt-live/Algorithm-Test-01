# 서랍의 비밀번호
a, b = list(map(int, input().split()))
if a > b:
    print(a - b + 1)
# 2043. 서랍의 비밀번호

a, b = list(map(int, input().split()))
sum = 0
if a > b:
    sum = a - b + 1
else:
    sum = b - a + 1
 
print(sum)
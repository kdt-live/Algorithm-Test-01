# 2043_서랍의비밀번호.py
# p = 123
# k = 100
p, k = map(int, input().split())
i = 0

for i in range(p-k+1):
    i += 1
    k += 1
    
print(i)
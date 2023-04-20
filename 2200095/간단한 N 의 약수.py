input_ = int(input())
res = [
    
]
for i in range(1, input_ + 1):
    if input_ % i == 0:
        res.append(i)
a = ' '.join(list(map(str, res)))
print(a)

    

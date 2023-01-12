# 1288 .새로운 불면증 치료법
T = int(input())

for i in range(1, T+1):
    sum = 0
    lst = []
    n = int(input())

    while len(lst) < 10:
        sum += n
        for j in str(sum):
            if j not in lst:
                lst.append(j)
    
    print(f'#{i} {sum}')
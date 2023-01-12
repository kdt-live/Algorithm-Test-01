case = int(input())

for i in range(1, case+1):
    num = input()
    temp = [] # 0~9
    a = 1
    while(len(temp) < 10):
        result = int(num) * a
        for n in str(result):
            if n not in temp:
                temp.append(n)
        a += 1
    print(f'#{i} {result}')
        
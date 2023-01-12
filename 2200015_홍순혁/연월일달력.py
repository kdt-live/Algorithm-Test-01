b = int(input())
q=0
w=0
e=0
for i in range(1,b+1):
    a = int(input())
    if a // 10000:
        q+=a//10000
    
    if a % 10000:
        w +=(a%10000)//100

    if a % 100:
        e +=a%100

    if w == 1 and 3 and 5 and 7 and 8:
        if e < 10:
            print(f'{q}/0{w}/0{e}')
        if 10 < e < 32:
            print(f'{q}/0{w}/{e}')

    if w == 10 and 12:
        if e < 10:
            print(f'{q}/{w}/0{e}')
        if e >= 10 :
            print(f'{q}/{w}/{e}')
        if e >= 32:
            print('-1')
    if w ==2:
        if e < 10:
            print(f'{q}/0{w}/0{e}')
        if e >= 10 :
            print(f'{q}/0{w}/{e}')
    if w >13:
        print('-1')
    if w == 4 and 6 and 9:
        if e < 10:
            print(f'{q}/0{w}/0{e}')
        if e >= 10 :
            print(f'{q}/0{w}/{e}')
        if e>= 31:
            print('-1')
    if w == 11:
        if e < 10:
            print(f'{q}/{w}/0{e}')
        if e >= 10 :
            print(f'{q}/{w}/{e}')
        if e>= 31:
            print('-1')




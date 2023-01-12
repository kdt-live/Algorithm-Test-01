T=int(input())
x=['01','03','05','07','08','10','12']
for i in range(1,T+1):
    a=input()
    b=a[4:6]
    c=a[6:]
    if int(b)> 0 and int(b) <=12:
        if b=='02':
            if int(c)>0 and int(c)<=28:
                print(f'#{i} {a[0:4]}/{b}/{c}')
            else:
                print(f'#{i} -1')
        else:
            if b in x:
                if int(c)>0 and int(c)<=31:
                    print(f'#{i} {a[0:4]}/{b}/{c}')
                else:
                    print(f'#{i} -1')
            else:
                if int(c)>0 and int(c)<=30:
                    print(f'#{i} {a[0:4]}/{b}/{c}')
                else:
                    print(f'#{i} -1')
    else:
        print(f'#{i} -1')
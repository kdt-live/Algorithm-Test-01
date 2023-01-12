#연월일 달력

a=int(input())
dic={
    '01':31,
    '02':28,
    '03':31,
    '04':30,
    '05':31,
    '06':30,
    '07':31,
    '08':31,
    '09':30,
    '10':31,
    '11':30,
    '12':31
}
for i in range(1,a+1):
    b=input()
    print(b)
    cnt=0
    
    print('#'+str(i),end=' ')
    if b[4]+b[5] in dic and int(b[6]+b[7])<=dic[b[4]+b[5]]:
        for b_ in b:
            print(b_,end='')
            cnt+=1
            if cnt ==4 or cnt==6:
                print('/',end='')
        print()
    else :
        print(-1)
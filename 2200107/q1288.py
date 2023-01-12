#1288. 새로운 불면증 치료법
import sys
sys.stdin = open("input.txt", "r")

T=int(input())
for tc in range(T):
    num=int(input())
    
    li=[]
    st_li=[]
    for a in range(10):
        st_li.append(str(a))
    # print(st_li)
    for n in range(1,100):
        mtp=num*n
        str_mtp=str(mtp)
        for a in str_mtp:
            if a not in li:
                li.append(a)
            # print(li)
            new_li=sorted(li)
            # print(new_li)
        if new_li==st_li:
            break
    # print(mtp)
    print(f'#{tc+1} {mtp}')
# 2043. 서랍의 비밀 번호
P,K= list(map(int,input().split()))

if P-K>0:
    print(P-K+1)
else:
    print(999-P+K)


# 2056. 연월일 달력
import sys
sys.stdin = open("input.txt", "r")

T=int(input())
for tc in range(1,T+1):
    str_date=input()
    new_date=[]
    for a in str_date:
        new_date.append(a)

    date=int(str_date)
    year=date//10000
    month=(date//100)%year
    day=date%100


    # def year():
    #     for a in range(4):
    #         print(new_date[a],end="")
    # def month():
    #     for a in range(4,6):
    #         print(new_date[a],end="")
    # def day():
    #     for a in range(6,8):
    #         print(new_date[a],end="")
    py=(new_date[0]+new_date[1]+new_date[2]+new_date[3])
    pm=(new_date[4]+new_date[5])
    pd=(new_date[6]+new_date[7])
    
    clear=f'#{tc} {py}/{pm}/{pd}'
    fail=f'#{tc} -1'

    # print(clear, fail)
    if month>12:
        print(fail)
    elif month==0:
        print(fail)
        continue
    if month==2:
            if day>29:
                print(fail)
            else:
                print(clear)
    else:
        if month==4 or 6 or 9 or 11:
            if day>31:
                print(fail)
        if month==1 or 3 or 5 or 7 or 8 or 10 or 12:
            if day>32:
                print(fail)
        if day==0:
            print(fail)
        print(clear)       

# 2072. 홀수만 더하기
import sys
sys.stdin = open("input.txt", "r")

T=int(input())
for tc in range(T):
    numbers=list(map(int,input().split()))
    sum=0
    for e in numbers:
        if e%2==0:
            continue
        else:
            sum+=e
    print(f'#{tc+1} {sum}')
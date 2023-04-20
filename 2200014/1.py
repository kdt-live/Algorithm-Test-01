#홀수만 더하기

a=int(input())

for i in range(a):
    cnt=0
    b=list(map(int,input().split()))
    for j in b:
        if j%2!=0:
         cnt+=j
    print('#'+str(i+1), cnt)
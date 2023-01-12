#서랍의 비밀번호

a,b=map(int,input().split())
if a>=b:
    print(a-b+1)
else:
    print(999-b+1+a)
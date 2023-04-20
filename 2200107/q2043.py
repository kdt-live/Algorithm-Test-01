# 2043. 서랍의 비밀 번호
P,K= list(map(int,input().split()))

if P-K>0:
    print(P-K+1)
else:
    print(999-P+K)
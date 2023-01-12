P, K = map(int, input().split())

if P-K > 0:
    print(P-K+1)
else:
    print(999-K+P+1)
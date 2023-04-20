#간단한 N의 약수
n=int(input())
re=[]
for i in range(1,n+1):
    if n%i == 0:
        re.append(i)
for i in range(len(re)):
    print(re[i],end=" ")
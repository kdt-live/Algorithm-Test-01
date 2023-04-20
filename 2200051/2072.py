#홀수만 더하기
t=int(input())
num=[]
result=[]
for i in range(t):
    sum=0
    num=list(map(int,input().split()))
    for j in range(10):
        if (num[j]%2)==1:
            sum += num[j]
    result.append(sum)
for i in range(t):
    print(f"#{i+1} {result[i]}")
p,k=list(map(int,input().split()))
sum=1

for number in range(k,p+1):
   if number!=p:
       sum=sum+1
print(sum)       
   
N = int(input())
arr = []
for i in range(1,N//2+1):
  if N%i==0:
    arr.append(i)
arr.append(N)
for a in arr:
  print(a,end=' ')
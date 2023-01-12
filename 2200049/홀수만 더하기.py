T = int(input())
for idx in range(T):
  arr = list(map(int,input().split()))
  sum = 0
  for a in arr:
    if a%2==1:
      sum+=a
  print(f"#{idx+1}",sum)
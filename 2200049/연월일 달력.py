T = int(input())
for idx in range(T):
  date = input()
  year = int(date[:4])
  month = int(date[4:6])
  day = int(date[6:])
  print(f"#{idx+1}",end=' ')
  if month>12 or month<1:
    print(-1)
    continue
  else:
    if month in [1,3,5,7,8,10,12]:
      if day<1 or day>31:
        print(-1)
        continue
    elif month in [4,6,9,11]:
      if day<1 or day>30:
        print(-1)
        continue
    elif month in [2]:
      if day<1 or day>28:
        print(-1)
        continue
  print("%04d/%02d/%02d" %(year,month,day))
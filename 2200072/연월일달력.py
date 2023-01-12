# 2056 연월일달력
t = int(input())
for i in range(t):
  day = str(input())
  if int(day[4:6]) >=1 and int(day[4:6]) <= 12 :
    if (int(day[4:6]) in [1,3,5,7,8,10,12]) and (int(day[-2:]) >= 1 and int(day[-2:]) <= 31) :
      print(f'#{i+1} {day[:4]}/{day[4:6]}/{day[-2:]}')
    elif (int(day[4:6]) == 2) and (int(day[-2:]) >= 1 and int(day[-2:]) <= 28) :
      print(f'#{i+1} {day[:4]}/{day[4: 6]}/{day[-2:]}')
    elif (int(day[4:6]) in [4,6,9,11]) and (int(day[-2:]) >= 1 and int(day[-2:]) <= 30) :
      print(f'#{i+1} {day[:4]}/{day[4: 6]}/{day[-2:]}')
    else :
      print(f'#{i+1} -1')
  else:
    print(f'#{i+1} -1')

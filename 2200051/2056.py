#연월일 달력
t=int(input())
result=[]
for i in range(t):
    n=input()
    y=n[:4]
    m=n[4:6]
    d=n[6:8]
    day={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    if (int(m)>=13) or (int(m)<=0):
        result.append(-1)
        continue
    else:
        if day[int(m)]<int(d) or int(d) <=0:
            result.append(-1)
            continue
        else:
            date=(y+'/'+m+'/'+d)
            result.append(date)
for i in range(t):
    print(f"#{i+1} {result[i]}")
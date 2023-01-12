T = 3 #int(input())

day = {'month' : list(range(1,13)), 'thirtyday' : list(range(1,31)), 'preday' : list(range(1,32)) , 'other' : list(range(1,29))}

for i in range(1,T + 1):
    date = 20000027 #input()
    if date[4:6] in str(day['month']):
        pass
    elif date[6:] in str(day['thirtyday']):
        pass
    elif date[6:] in str(day['preday']):
        print(-1)
        pass
    elif date[6:] in str(day['other']):
        pass
    elif len(date) == 8:
        pass
    else:
       print(-1)
       date = 0
       continue
    date = 0

print(f'#{i}')
print(str(date)[0:4], str(date)[4:6], str(date)[6:],sep ='/')

# 불면증 치료법  
T = int(input())
cnt = 0
for t in range(1, T+1) :
    n = int(input()) #n 1295
    cnt_li = []
    
    while len(cnt_li) != 10 :           
        li = []
        b=1
        new = n
        while b!=0 :        
            b = new % 10
            new = new//10
            li.append(b)    
        li_re = li[::-1]
        li_re.pop(0) #li_re [1, 2, 9, 5]
                            
        for i in li_re :
            if i not in cnt_li :
                cnt_li.append(i)
                print(cnt_li)
        cnt += 1        
        n *= 2

    print(f'#{t} {cnt}')

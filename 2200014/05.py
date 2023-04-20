#양 세기

a=int(input())
for i in range(1,a+1):
    b=int(input())
    cnt=0
    list1=[]
    num=1
    while len(list1)!=10:
        N=b
        N=N*num
        for j in str(N):
            if j not in list1:
                list1.append(j)
                
        cnt+=1
        # print(N,list1,cnt)    
        
        num+=1
        
    print('#'+str(i),N)
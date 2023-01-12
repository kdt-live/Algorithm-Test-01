# import sys
# sys.stdin = open("input.txt", "r")

a = int(input())
d30 = [4,6,9,11]
d31 = [1,3,5,7,8,10,12]
for i in range(a):
    b = input()
    y= b[0]+b[1]+b[2]+b[3]
    m= b[4]+b[5]
    d= b[6]+b[7]
    if int(m)>12 or int(m)<1 or int(d)<1:
        print(f'#{i+1} -1')
    elif int(m)==2 and int(d)>28:
        print(f'#{i+1} -1')
    elif int(m) in d30 and int(d)>30:
        print(f'#{i+1} -1')
    elif int(m) in d31 and int(d)>30:
        print(f'#{i+1} -1')      
    else:
        print(f'#{i+1} {y}/{m}/{d}')
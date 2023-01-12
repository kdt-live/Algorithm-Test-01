input_str = input()
input_int = int(input_str)
res = [

]
cnt = 1
while(True):
    for i in str(input_int * cnt):
        res.append(i)
        res = list(set(res))
        print(res)
        
    if len(res) == 10:
        break
    
print(cnt)




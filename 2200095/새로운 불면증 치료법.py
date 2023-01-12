input_str = input()
input_int = int(input_str)
res = [

]
cnt = 1
while(True):
    for i in str(input_int * cnt):
        res.append(i)
        list(set(res))
        cnt += 1
        if len(res) == 10:
            break

        print(cnt)
print(res)



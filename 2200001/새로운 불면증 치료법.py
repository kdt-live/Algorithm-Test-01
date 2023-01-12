# 새로운 불면증 치료법
T = int(input())

for t in range(1, T+1):
    N = int(input())
    cnt = 1
    result_list = [] 

    while (len(result_list) < 10):
        number = cnt * N
        cnt += 1
        for m in str(number):
            if m not in result_list:
                result_list.append(m)
    
    print(f"#{t} {number}")
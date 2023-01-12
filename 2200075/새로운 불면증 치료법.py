T = int(input())

for t in range(1, T+1):
    N = int(input())
    num_list = set()
    cnt = 1

    while 10 > len(num_list) :
        number = str(N * cnt)
        for num_one in number:
            num_list.add(num_one)
        result = N * cnt
        cnt += 1 
    print(f'#{t} {result}')
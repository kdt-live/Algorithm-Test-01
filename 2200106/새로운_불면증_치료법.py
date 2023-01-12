T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    num_list = set()
    cnt = 1
    while num_list != set(range(10)):
        now = cnt * n
        for i in str(now):
            num_list.add(int(i))
        cnt += 1
    print(f'#{test_case} {now}')


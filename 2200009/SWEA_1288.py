i_t = int(input())
for i_1 in range(i_t):
    i_n = int(input())
    set_mult = set()
    i_cnt = 0
    while set_mult != set(range(10)):
        i_cnt += 1
        i_mult = i_n * i_cnt
        s_mult = str(i_mult)
        for s_1 in s_mult:
            set_mult.add(int(s_1))
    print(f'#{i_1 + 1} {i_cnt*i_n}')
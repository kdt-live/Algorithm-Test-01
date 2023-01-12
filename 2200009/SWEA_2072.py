i_t = int(input())
for i_1 in range(i_t):
    i_sum_odd = 0
    lst_input = list(map(int, input().split()))
    for i_2 in lst_input:
        if i_2 %2 == 1:
            i_sum_odd += i_2
    print(f'#{i_1 +1} {i_sum_odd}')
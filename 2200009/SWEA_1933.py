i_n = int(input())
lst_div = []
for i_1 in range(1, i_n + 1):
    if i_n % i_1 == 0:
        lst_div.append(i_1)
print(*lst_div)
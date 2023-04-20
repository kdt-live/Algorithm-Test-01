T = int(input()); cnt = 0; sum_odd = []
for i in range(T):
    numbers = list(map(int,input().split()))
    for i in range(len(numbers)):
        if numbers[i] % 2 == 1: cnt += numbers[i]
        else: pass
    sum_odd.append(cnt); cnt = 0
for i in range(T): print("#{} {}".format(i+1, sum_odd[i]))
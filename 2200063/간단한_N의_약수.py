# 입력으로 1개의 정수 N이 주어진다.
# 정수 N의 약수를 오름차순으로 출력하는 프로그램을 작성하라.

# 1 <= N <= 1000 int

import math

N = int(input())
n_list = []
for n in range(1, N+1):
    num = math.trunc(N / n)
    if num*n == N:
        n_list.append(num)
print(*sorted(n_list))
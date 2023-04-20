# 간단한 N의 약수
N = int(input())
N_list = []
for n in range(1, N+1):
    if N % n == 0: # n을 N으로 나눴을 때 0이 되면 n은 N의 약수
        N_list.append(n)
    else:
        continue
for i in N_list:
    print(i, end=" ")
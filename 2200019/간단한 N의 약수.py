N = int(input())
N_list = []

for i in range(1,N+1):
    if N%i == 0:
        N_list.append(i)
        
print(*N_list)
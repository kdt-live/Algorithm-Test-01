T = int(input())

numbers = [3,17, 1, 39, 8, 41, 2, 32, 99, 2] # list(map(int,input().split()))  [map(int,input().split())] [3,17, 1, 39, 8, 41, 2, 32, 99, 2]

for i in range(1,T + 1):
    odd = 0
    numbers = list(map(int,input().split()))
    for k in numbers:
        if k % 2 == 1:
            odd = odd + k
        else:
            pass

    print(f'#{i}', odd)
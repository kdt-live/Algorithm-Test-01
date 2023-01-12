# 2072_홀수만 더하기.py
T = int(input())

#numbers = [3, 17, 1, 39, 8, 41, 2, 32, 99, 2,]
n = 0
for test_case in range(1, T + 1):
    numbers=map(int, input().split())
    for result in numbers:
        if result%2 == 1:
            #print(result)
            n += result
            #print(n)
    print(f'#{test_case} {n}')
    n=0

T = int(input())
for test_case in range(1, T + 1):
    a = set()
    b = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    cnt = 1
    N = int(input())
    while a != b:
        i = str(N * cnt)
        a.add(i)
        cnt += 1
    if a == b:
        break
    print(cnt)
    
    
    
    
# k = list(map(str, input()))
# print(k)
    # while True:

    
    # for i in N:
    #     print(i)
    


# print(f'#{test_case} {result}')

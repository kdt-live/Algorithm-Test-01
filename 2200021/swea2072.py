# 2072 홀수만 더하기

for i in range(1,int(input())+1):
    nums = list(map(int,input().split()))
    sum = 0
    for n in nums:
        if n % 2 == 1:
            sum += n
    print(f'#{i} {sum}')
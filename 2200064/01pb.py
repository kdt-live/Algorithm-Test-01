# 10개의 숫자를 입력받고 홀수만 더하기

T = int(input())

for t in range(1, T+1):
    nums = map(int, input().split())
    result = 0
    for i in nums:
        if i%2 != 0:
            result += i
    print(f'#{t} {result}')

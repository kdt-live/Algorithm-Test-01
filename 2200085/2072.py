# 테스트 케이스 입력
T = int(input())

# 테스트 케이스마다 10 개 수 입력
for t in range (1, T+1):
    nums = list(map(int, input().split()))
    sum = 0

    # 입력 리스트에서 홀수인 수끼리 합 구하기
    for num in nums:
        if (num % 2 == 1):
            sum += num

    print(f'#{t} {sum}')
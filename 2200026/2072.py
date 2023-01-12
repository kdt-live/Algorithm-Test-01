# 2072 홀수만 더하기
# 테스트 케이스 수
T = int(input())  # 3
for t in range(1, T+1):
    # 홀수만 더하는 코드
    num = list(map(int, input().split()))
    cnt = 0
    for n in num:
        if n % 2 != 0:
            cnt += n
    print(f'#{t} {cnt}')

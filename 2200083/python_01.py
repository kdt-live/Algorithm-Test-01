# 홀수만 더하기
# 10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.
# 3
# 3 17 1 39 8 41 2 32 99 2
# 22 8 5 123 7 2 63 7 3 46
# 6 63 2 3 58 76 21 33 8 1 

T = int(input())
for t in range(1, T+1):
    numbers = list(map(int, input().split()))
    total = 0
    for num in numbers:
        if num%2 == 1:
            total += num
    print(f'#{t} {total}')
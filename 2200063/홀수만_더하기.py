# 10개의 수를 입력받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램 작성
# 가장 첫 줄에 테스트 케이스 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.

# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.

T = int(input())


for t in range(1, T+1):
    result = 0
    numbers = list(map(int, input().split()))
    for n in numbers:
        if n % 2 == 1:
            result += n
           
    print(f'#{t} {result}')
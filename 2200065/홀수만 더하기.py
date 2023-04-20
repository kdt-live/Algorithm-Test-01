# 홀수만 더하기


# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.


t = int(input())
m= []

for i in range(1,t+1):
    n = list(map(int,input().split()))
    for a in n:
        if a % 2 == 1:
            m.append(a)
    print(f'#{i}',sum(m))
    m = []
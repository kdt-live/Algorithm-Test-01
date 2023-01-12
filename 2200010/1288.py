# [입력]

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 N (1 ≤ N ≤ 106)이 주어진다.

# [출력]

# 각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며
#  1부터 시작한다)를 출력하고,
# 최소 몇 번 양을 세었을 때 이전에 봤던 숫자들의 자릿수에서
#  0에서 9까지의 모든 숫자를 보게 되는지 출력한다.
# ( 민석이는 xN번 양을 세고 있다. )

# import sys
# sys.stdin = open('data/새로운 불면증 치료법.txt', 'r')

T = int(input())
nums = set()
absolute_nums = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

for t in range(1, T + 1): # 케이스 반복(okay)
    N = int(input()) # 입력 (okay)
    a = N
    cnt = 1 # 초기값 설정 (okay)
    while nums != absolute_nums:
        while a > 0:
           b = a % 10 
           a = a // 10
           nums.add(b)
        cnt += 1
        a = N * cnt
    print(cnt)
import sys
sys.stdin = open('EXAM-01/2200082/input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    nums = list(map(int, input().split()))
    odds = [n for n in nums if n%2 == 1]
    print(f'#{t} {sum(odds)}')
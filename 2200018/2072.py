# 홀수만 더하기
import sys

sys.stdin = open('input_2072.txt')

T = int(input())

for i in range(T):
    a = [i for i in map(int, input().split()) if i % 2 == 1]
    print(f'#{i+1} {sum(a)}')

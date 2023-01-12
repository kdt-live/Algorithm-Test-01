# 서랍의 비밀번호
import sys

sys.stdin = open('input_2043.txt')

a, b = map(int, input().split())
print(a % b + 1)
import sys
sys.stdin = open('EXAM-01/2200082/input.txt', 'r')

N = int(input())
candid = list(range(1, N+1))
measure = []
for n in candid:
    if N % n == 0:
        measure.append(n)

print(*measure)
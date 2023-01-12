import sys
sys.stdin = open('EXAM-01/2200082/input.txt', 'r')

P, K = input().split()

p = int(P)
k = int(K)

tried = 0
while True:
    tried += 1
    if p == k:
        break
    else:
        k += 1
    if k == 1000:
        k = 0
print(tried)
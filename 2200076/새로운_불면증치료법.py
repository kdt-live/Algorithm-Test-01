import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    sheep = int(input())
    sheep_n = 0
    nums = []
    while len(nums) < 10:
        sheep_n += sheep
        for a in str(sheep_n):
            if a in nums:
                continue
            else:
                nums.append(a)
        
    print(f'#{t} {sheep_n}')
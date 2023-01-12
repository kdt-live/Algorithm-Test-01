import sys
sys.stdin = open('EXAM-01/2200082/input.txt', 'r')

# 이전에 셌던 번호들의 각 자리수에서 0에서 9까지의 모든 숫자를 보는 것은 최소 몇 번 양을 센 시점일까?
# 각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
# 최소 몇 번 양을 세었을 때 이전에 봤던 숫자들의 자릿수에서 0에서 9까지의 모든 숫자를 보게 되는지 출력한다.
# ( 민석이는 xN번 양을 세고 있다. )

# xN 번 세고 있다 -> 

T = int(input())

for t in range(1, T+1):
    N = int(input())
    cycle = 0
    nums_set = set()
    sheep_no = N
    while True:
        cycle += 1
        sheep = str(sheep_no)
        for char in sheep:
            nums_set.add(char)
        if len(nums_set) == 10:
            print(f'#{t} {N * cycle}')
            break
        sheep_no += N









    # N = int(input())
    # cycle = 0
    # all_numbers = []
    # sheep = N
    # while True:
    #     cycle += 1
    #     nums = list({k:v for v, k in enumerate(str(sheep))})
    #     for elm in nums:
    #         all_numbers.append(elm)
    #     all_numbers = list(dict.fromkeys(all_numbers))
    #     if len(all_numbers) == 10:
    #         break
    #     sheep += N
    # print(f'#{t} {cycle}')




# nums = {k:v for k, v in enumerate('12345')}
# print(*list(nums.values()))
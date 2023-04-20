T = int(input())

for t in range(1, T + 1):
    nums = list(map(int, input().split()))
    lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for n in nums:
        if nums[4:5] in lists:
            print(nums)
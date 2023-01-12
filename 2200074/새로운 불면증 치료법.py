T = int(input())

for t in range(1, T+1):
    N = int(input())
    nums = []
    i = 1

    while True:
        new_N = N * i
        string_num = str(new_N)

        if sorted(nums) != list(range(10)):
            for c in string_num:
                if int(c) not in nums:
                    nums.append(int(c))
        else:
            print(f'#{t} {new_N-N}')
            break
        
        i += 1
       
    

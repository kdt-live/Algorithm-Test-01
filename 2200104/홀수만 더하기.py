T = int(input())

for test_case in range(1, T + 1):
    
    num_sum = 0
    numbers = map(int, input().split())
    
    for num in numbers:
        if num % 2 == 1:
            num_sum += num
        
    print(f"#{test_case}", num_sum)
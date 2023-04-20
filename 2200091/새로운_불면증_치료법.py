test = int(input())

for i in range(test):
    numbers = {}
    ship = int(input())
    n = ship
    cnt = 1

    while len(numbers) != 10:
        while n > 0:
            if n%10 not in numbers:
                numbers[n%10] = 1

            n //= 10
        
        cnt += 1
        n = cnt * ship

    print(f"#{i+1} {n-ship}")

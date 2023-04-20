T = int(input())

for t in range(1,T+1) :
    numbers = list(map(int,input().split()))
    sum = 0
    for i in range(0, len(numbers)) :
        if numbers[i] % 2 == 1 :
            sum += numbers[i]
    print(f"#{t} {sum}")
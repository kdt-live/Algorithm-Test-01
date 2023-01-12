num = int(input())
i = 1

while num >= i:
    if num % i == 0:
        print(i, end=" ")
    
    i += 1
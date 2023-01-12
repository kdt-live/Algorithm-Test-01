T = int(input())
numbers = (1,2,3,4,5,6,7,8,9,0)
number = ()
i = 1
for a in range(1, T + 1):
    if number != numbers:
        i *= a
        print(f'#{a} {i}')
    else:
        print(f'#{a} {i}')
        break
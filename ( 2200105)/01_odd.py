# 10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.

# number = list(map(int,input('숫자 입력: ').split()))
# print(number)

# odd = number % 2, 1
# even = number % 2, 0

T = int(input('테스트 케이스: '))
i = 0
sum = 0


for t in range(1,T + 1):
    N = int(input('입력 줄 수: '))
    for _ in range(N):
        number = list(map(int,input('숫자 입력: ').split()))
        # for i in number:
        #         if (i % 2) == 0:
        #          sum += i
        
        

      
        # if t in number % 2 != 0:
        #     continue 
        print(number)
        # print(odd)
        print('#', N , sum(number))
        # for i in range(number):
        #     if i % 2 == 1:
        #         print(sum(i))


        


    # if number%2 == 1
    # else:
    #     even = number%2 == 0
    

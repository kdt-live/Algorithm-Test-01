# T = int(input())
# for test_case in range(1, T + 1):

#     numbers = list(map(int,input().split()))
#     sum = 0
#     for i in numbers:
#         if i % 2 == 1:
#             sum += 1
#     print("#{} {}".format(test_case, sum))

T = int(input())
for test_case in range(1, T+1):
    numbers = list(map(int,input().split()))
    test_case_sum = 0
    for i in numbers:
        if i % 2:
            test_case_sum += i
    print("#{} {}".format(test_case, test_case_sum))

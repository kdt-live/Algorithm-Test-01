import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

result_list = ['0', '1', '2', '3','4','5','6','7','8','9']

for t in range(1, T + 1):
    num = int(input())
    list = []
    j = 1
    while j > 0:
        a = num * j 
        for i in str(a):
            list.append(i)
        j += 1
        if sorted(set(result_list)) == sorted(set(list)):
            break
    print(f"#{t} {a}")
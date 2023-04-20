# 양을 N의 배수로 센다
# 첫번 째에는 N번 양을 세고, 두 번째에는 2N번 ... k번째에는 kN번의 양을 센다
# 셌던 번호들의 각 자리수에서 0~9까지의 모든 숫자를 보는 것은 최소 몇 번 양을 센 시점일까
# ex) N = 1295 가정할 때 첫 번째는 N = 1295 (1, 2, 5, 9) 두 번째는 2N = 2590 (0, 2, 5, 9) ....

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다
# 각 테스트 케이스의 첫 번째 줄에는 N이 주어진다

# 각 테스트 케이스마다 '#x'를 출력
# 최소 몇 번 양을 세었을 때 이전에 봤던 숫자들의 자릿수에서 0~9까지의 모든 숫자를 보게 되는지 출력한다.

T = int(input())

n1_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for t in range(1, T+1):
    n2_list = []
    N = int(input())
    M = N
    while True:
        if n2_list != n1_list:
            for n in str(M):
                if int(n) not in n2_list:
                   n2_list.append(int(n))
                   n2_list = sorted(n2_list)
            M += N
    
        else:
            M -= N
            break
    print(f'#{t} {M}')
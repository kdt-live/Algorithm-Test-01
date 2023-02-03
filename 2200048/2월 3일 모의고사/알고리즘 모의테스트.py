# 1218 괄호 짝짓기
import sys

for i in range(1,11):
    T = int(sys.stdin.readline().strip())
    a = list(sys.stdin.readline().strip())
    for k in a:
        stack = k # 값을 비교하기 위한 기준점 지정
        if stack == k:
            result = 0
            break
        else:
            result = 1
            continue
    print(f'#{i} {result}')

# 1225 암호생성기

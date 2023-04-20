# 1933. 간단한 약수
# 약수란 어떠한 수를 나누어 떨어지게 하는 수
num = int(input())  # 하나의 정수 입력

for n in range(1, num+1):
    if num % n == 0:
        print(n, end=" ")

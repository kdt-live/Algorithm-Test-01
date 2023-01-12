# 간단한 N 의 약수
# 입력으로 1개의 정수 N 이 주어진다.
# 정수 N 의 약수를 오름차순으로 출력하는 프로그램을 작성하라.
# 입력 : 10 출력 : 1 2 5 10

number = int(input())

for num in range(1, number+1):
    if number % num == 0:
        print(num, end=" ")
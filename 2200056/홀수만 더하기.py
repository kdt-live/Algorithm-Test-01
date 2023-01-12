# 10개의 수를 입력 받아, 그 중에서 홀수만 더한 값 출력
T = int(input())

for t in range(1, T + 1):
    number_list = map(int, input().split()) # 10개의 수 입력받기
    add = 0
    for number in number_list: # 10개 수 순환
        if number % 2 == 0:
            continue
        else:
            add += number # 홀수면 더하기
    print("#{0} {1}".format(t, add))
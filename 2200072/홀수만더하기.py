# 2072 홀수만 더하기

t = int(input())

for i in range(t):
  sum = 0
  numbers = list(map(int, input().split()))
  for number in numbers:
    if number%2 == 1:
      sum += number
  print(f'#{i+1} {sum}')
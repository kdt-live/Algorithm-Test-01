# 1288 새로운 불면증 치료법

t = int(input())

for i in range(t):
  n = input()
  N = int(n)
  one_ten_dict = {}
  cnt = 1

  while len(one_ten_dict.keys()) < 10:
    for num in n:
      one_ten_dict[num] = 1
      n = str(cnt*N)
    cnt += 1

  print(f'#{i+1} {int(n)-N}')
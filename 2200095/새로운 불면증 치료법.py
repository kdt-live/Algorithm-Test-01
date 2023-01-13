T = int(input())
for t in range(1, T + 1):
   input_ = input()
   cnt = 0
   res = []
   while True:
      cnt += 1
      input_2 = str(int(input_) * cnt)
      for i in input_2:
         res.append(i)
         res = list(set(res))
         res.sort()
      if len(res) == 10:
         print(f'#{t} {input_2}')
         break



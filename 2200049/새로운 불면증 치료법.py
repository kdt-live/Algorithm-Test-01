#N의 배수

T = int(input())
arr = [False for i in range(10)]

def check():
  for i in range(10):
    if arr[i]==False:
      return False
  return True

for idx in range(T):
  N = input()
  tmp = int(N)
  k = 1
  #초기화
  for i in range(10):
    arr[i]=False
  #현재 본 숫자 체크
  while True:
    for s in range(len(N)):
      arr[int(N[s])]=True
    
    #0부터 9까지 모두 봤는지 체크
    if check():
      print(f"#{idx+1}",N)
      break
    N = str(tmp*(k+1))
    k+=1
    #print("N",N)



'''
T = int(input())

arr = [False for i in range(0,10)]

def check():
  for i in range(0,10):
    if arr[i]==False:
      return False
  return True

for idx in range(T):
  N = input()
  tmp = N
  k = 1
  while True:
    for s in range(len(N)):
      if arr[int(N[s])]==False:
        print("N[s]",N[s])
        arr[int(N[s])]=True
        print(arr)

        if check():
          return

    N=str(int(tmp)*k)
    k+=1
    print("N",N)
  print(k)
'''
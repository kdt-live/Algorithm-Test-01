# 간단한 N의 약수

number = int(input())

for t in range(1, number+1):
    if number % t == 0 :
        
        print(t)

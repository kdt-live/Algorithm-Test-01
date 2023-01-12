# 간단한 N의 약수
a = int(input())
for i in range(1, a+1) :
    if a%i == 0 :
        print(i, end=" ")    
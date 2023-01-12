#1933. 간단한 N 의 약수
a = int(input())
b = []
for i in range(1, a+1):
    if a%i == 0:
        b.append(i)
for i in b:
    print(i, end=" ")
p, k = map(int, input().split())

#print(p+1-k) 이것도 가능하지만 반복문을 써봅시당

answer = 1
while(k < p):
    k += 1
    answer += 1
print(answer)
P, K = map(int, input().split())
    
area = K - P

if area < 0:
    area = -area

print(area+1)
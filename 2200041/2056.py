# 문제풀이 코드
t = int(input())
for T in range(1, t+1):
    ns = input()
    yyyy = ns[0:4]
    mm = ns[4:6]
    dd = ns[6:8]
    if int(mm) == 0:
        print(f'#{T} {-1}')
    elif int(mm) <= 12:
        if int(mm) <= 7:
            if int(mm) % 2 == 1:
                if int(dd) > 31:
                    print(f'#{T} {-1}')
                else:
                    print(f'#{T} {yyyy}/{mm}/{dd}')
                 
            elif int(mm) == 2:
                if int(dd) > 28:
                    print(f'#{T} {-1}')
                else:
                    print(f'#{T} {yyyy}/{mm}/{dd}')
            else:
                if int(dd) > 30:
                    print(f'#{T} {-1}')
                else:
                    print(f'#{T} {yyyy}/{mm}/{dd}')
        else:
            if  int(mm) % 2 == 0:
                if int(dd) > 31:
                    print(f'#{T} {-1}')
                else:
                    print(f'#{T} {yyyy}/{mm}/{dd}')
                     
            else:
                if int(dd) > 30:
                    print(f'#{T} {-1}')
                else:
                    print(f'#{T} {yyyy}/{mm}/{dd}')
 
    else:
        print(f'#{T} {-1}')
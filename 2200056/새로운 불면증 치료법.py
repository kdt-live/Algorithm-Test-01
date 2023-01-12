# 민석이의 불면증 양세기 N의 배수로 0123456789 보면 끝
T = int(input())

for t in range(1, T+1):
    N = input()
    
    N_list = []
    break_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    for n in range(1, 9999999999999999999999999):   # ㅎㅎ....
        if N_list == break_list:    # 민석이가 0123456789를 다 보면 break해주기
            break
        else:
            Nn = int(N) * n     # N의 배수 구하기
            Nn = str(Nn)        # N의 배수 숫자 하나 하나 씩 리스트에 넣어주기 위해서 str로 바꾸기
        
            for i in Nn:            # str이 된 N의 배수 요소 하나하나 리스트에 넣어주기
                if i in N_list:     # 근데 리스트에 이미 있으면 continue해주고
                    continue
                else:               # 그게 아니면 리스트에 추가하기
                    N_list.append(i)
                    N_list.sort()       # 이게 없으면 정렬 없이 숫자가 들어가서 break_list와 비교가 안됨
    
    print("#{0} {1}".format(t, Nn))     # 프린트 해주기

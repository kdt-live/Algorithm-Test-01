# 해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면
# [그림1] 과 같이 ”YYYY/MM/DD”형식으로 출력하고,
# 날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라.
# 연월일로 구성된 입력에서 월은 1~12 사이 값을 가져야 하며
# 일은 [표1] 과 같이, 1일 ~ 각각의 달에 해당하는 날짜까지의 값을 가질 수 있다.
# ※ 2월의 경우, 28일인 경우만 고려한다. (윤년은 고려하지 않는다.)
# [입력]
# 입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
# 다음 줄부터 각 테스트 케이스가 주어진다.
# [출력]
# 테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

num = input()

year = num[0:4]
month = num[4:6]
day = num[6:8]

T = int(input()) # 테스트 케이스 수

for t in range(1, T+1):
    N = int(input()) # 입력 줄 수
    
    for i in range(1,1+N):
        print(i)


        for i in num:
            if int(month) == 1 and int(day) >32:
                print(-1)
#             elif int(month) == 2 and int(day) >29:
#                 print(-1)
#             elif int(month) == 3 and int(day) >32:
#                 print(-1)
#             elif int(month) == 4 and int(day) >31:
#                 print(-1)
#             elif int(month) == 5 and int(day) >32:
#                 print(-1)
#             elif int(month) == 6 and int(day) >31:
#                 print(-1)
#             elif int(month) == 7 and int(day) >32:
#                 print(-1)
#             elif int(month) == 8 and int(day) >32:
#                 print(-1)
#             elif int(month) == 9 and int(day) >31:
#                 print(-1)
#             elif int(month) == 10 and int(day) >33:
#                 print(-1)
#             elif int(month) == 11 and int(day) >31:
#                 print(-1)
#             elif int(month) == 12 and int(day) >32:
#                 print(-1)
           
            
#                 print(year+'/'+month+'/'+day)
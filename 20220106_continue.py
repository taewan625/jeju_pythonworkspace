
# 점수리스트 = [65,47,89,93,56,78]
# 번호 = 0                            # 전역변수   # 1만 반복되는 것을 방지
# for 반복변수 in 점수리스트 :
#     번호 = 번호 + 1  # = 번호+=1
#     if 반복변수 >=60 :
#         print(번호,'번 :', 반복변수, '합격', end=' ') # True 인 경우 한 줄에 출력 end=''
#     else : 
#         print(번호, '번:', 반복변수, '불합격', end=' ')

# 합격자만 통보
# 방법 1
점수리스트 = [65,47,89,93,56,78]
번호 = 0
for 반복변수 in 점수리스트 :
    번호 = 번호 + 1  # = 번호+=1
    if 반복변수 >=60 :
        print(번호,'번 :', 반복변수, '합격')

# 방법 2 continue -> for 문의 처음으로 돌리게 하는 기능
점수리스트 = [65,47,89,93,56,78]
번호 = 0
for 반복변수 in 점수리스트 :
    번호 = 번호 + 1      # = 번호+=1
    if 반복변수 < 60 :   # 60 미만이면 돌아가서 다음 데이터를 비교함
        continue
    print(번호,'번 :', 반복변수, '합격')   # if 문과 맞춰서 써야 함


# 내장함수 builtin function
# 절대값 abs(데이터) <- absolute

'''num = -15
abs(num)
r = abs(num)
r 비교'''


print(-10) # -10 출력
print(abs(-10)) # -10의 절대값 

data = -25 # 데이터 입력
r = abs(data) # 입력된 데이터를 유사한지 절대값 구하기
# 결과 r 이 유사한지 비교
print(r)

# 들여쓰기 : 첫 시작 칸 맞추어야 indentation Error가 뜨지 않는다

# 최대값 max()
max(1, 2)
print(max(1,2))

data = 4, 3, 7, 234, 747, 23, 5, 23 
print(max(data))

#최대값 = 54 나오게 출력
print('최대값은', str(max(data))+'입니다' ) # 같은 형식끼리만 +가 가능하다
print('최대값은', max(data), '입니다')

# 최소값 min()
print(min(data))

# pow() 제곱 구하기
# 방법 1 : 수식을 이용
print(2**3)
# 방법 2 : 내장함수 pow() 이용
print(pow(2,3))

# 실습
# 입력된 데이터의 2의 x 승을 구하려한다.
제곱 = 10
print(pow(2, 제곱))

# 반올림 round()
i = 2.12
print(round(i))

# 합계 sum()
data = 1,3,4,5,3
print(sum(data))

# 몫과 나머지 : 수식기호 몫 // 나머지 %  # print(3//2, 3%2)
# 기호 divmod
print(divmod(3,2))
a = 3
b = 2

# 한 줄에 코딩
a,b,c = 1,2,3  # 왼쪽엔 무조건 변수, 오르쪽은 값
print(divmod(a,b))

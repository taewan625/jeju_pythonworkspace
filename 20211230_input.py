# 사용자로부터 입력 받기 함수 input(), str() 형태

# 방법 1 : input()
value = input()
# 문자로 인식되는 경우
value = input()
print('입력된 데이터:', value)
# 숫자로 계산해야되는 경우
number = input()
print('입력된 값* 100한 결과:', int(number)*100)  # input의 값은 문자로 인식하여 int함수를 넣어야 함

# 방법 2 : input('y나 n 중에 선택하세요')
answer = input('y나 n 중에 선택하세요')
print(answer+' 을 선택했습니다')


# 문자열 합치기
x = input('x 입력 :')
y = input('y 입력 :')
print(x+y)                              # 문자열 합치기

# 숫자열 합치기 1
x = input('x 숫자입력 :')
y = input('y 숫자입력 :')
print('x와 y의 합은 : ', int(x)+int(y)) # 숫자열 합치기

# 숫자열 합치기 2
x = input()
# print(f'사용자의 입력데이터 : {x}')
# 숫자로 계산해야되는 경우
print(f'사용자의 입력데이터 : {int(x)*100}')

# 숫자열 합치기 3
x = int(input('x 숫자입력 :'))
y = int(input('y 숫자입력 :'))
# print('x와 y의 합은 : ', x+y, '입니다') # 숫자열 합치기
print(f'{x} 과 {y} 의 합은 {x+y}입니다')                   # f 포맷 활용

# 실습(12/5일 중간고사에 적용)
'''
두 개의 버스 번호를 입력 받아 아래와 같이 출력 (단 f 포맷 활용)
[입력]
1번 버스 번호 입력 :
2번 버스 번호 입력 :
[출력]
(1번버스번호), (2번버스번호)  번 버스가 잠시 후 도착합니다. 
'''
x = input('1번 버스 번호 입력 :')
y = input('2번 버스 번호 입력 :')
print(f'{x}, {y}번 버스가 잠시후 도착합니다.')

# 정답: 여러개 문자를 한번에 쓸 때 처음은 소문자로 하고 그 이후 단어별로 첫글자만 대문자로 설정해야함_낙타표기법
fristBusNumber = input('1번 버스 번호 입력 :')
seconeBusNumber = input('2번 버스 번호 입력 :')
print(f'{fristBusNumber}, {seconeBusNumber}번 버스가 잠시 후 도착합니다.' )


# format(변수명)
yourName = '홍길동'
yourAge = 21
print("사용자의 이름은", yourName, '입니다')  # 방법 1 : comma 사용, 문자 나열
print('영웅의 이름은'+ yourName+ '입니다')    # 방법 2 : + 연산자 , 문자열 합치기
print(f'당신의 이름은 {yourName} 입니다')     # 방법 3 : f 포맷사용

print('입력된 이름은 {}, 나이는{} 입니다'. format(yourName,yourAge))         # 방법 4 : format()
print('입력된 이름은 \'{}\', 나이는{} 입니다'. format(yourName,yourAge))     # 방법 4 : format() ' ' 일 때 '' 사용 -> \' \'
print("입력된 이름은 '{}', 나이는{} 입니다". format(yourName,yourAge))       # 방법 4 : format() " " 일 때 '' 사용 -> 그냥 사용
print("입력된 이름은 '{1}', 나이는{0} 입니다". format(yourName,yourAge))        # 방법 4 : format() format( , ) 안의 순서는 0, 1 이므로 {}, {} 안에 0 1 을 넣으면 순서에 맞게 쓸수 있고 번호 생략시 차례대로

'''
실습 2
[입력]
좋아하는 과일 두가지를 입력(input()) 받아 format() 을 이용하여 아래와 같이 출력하세요
[출력]
당신이 좋아하는 과일은 ~과 ~ 입니다.
'''
favoriteFruitOne = input('좋아하는 과일1 입력 : ')
favoriteFruitTwo = input('좋아하는 과일2 입력 : ')
print('당신이 좋아하는 과일은 {}, {}입니다'.format(favoriteFruitOne, favoriteFruitTwo))
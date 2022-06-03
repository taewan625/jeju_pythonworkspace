# 문자열 포맷

# 방법 1

s = '제주대학교'

print(s)

# 제주대학교는 제주에 있는 국립대학교입니다.
print(s,'는 제주에 있는 국립대학교입니다.')    # 문자열을 나열 comma

# 방법 2
print(s + '는 제주에 있는 국립대학교입니다.')  # 문자열 합치기

# 방법 3 
print('%s 는 제주에 있는 국립대학교입니다.' % '제주대학교')   # %s -> 문자열 , 

# 방법 3 
print('고객님의 PIN 번호는 %d 입니다.' % 5432)                # %d -> 정수

# 방법 3
print('Apple 의 첫 문자는 A 입니다')                          # %c -> 문자
print('Apple 의 첫 문자는 %c 입니다' %'A')
print('%s 의 첫 문자는 %c 입니다' %('Apple', 'A'))

# %s %d
print('고객님의 예약번호는 %s 이며, pin 번호는 %d 입니다' %('oz12345', 1234))

# 방법 4 .format(변수)
'''
format 메소드
객체.format(내용)
    ↑                      ; 마침표 주의!!
객체.format(변수)
    ↑  
객체.format(변수=값)
    ↑ 
'''

print('{}는 제주에 있는 국립대학교입니다'.format('제주대학교'))
print('{}는 제주에 있는 {}입니다'.format('제주대학교','국립대학교'))

# 주문번호, 주문내역, 수량
o_no = 1
o_contents = '스위트버거'
o_qty = 2

'''
고객님의 
주문번호는 : 번
주문내용은 : 
wnanstnfid : 개
'''

print('고객님의 \n주문번호 : {}번\n주문내용 : {}\n주문수량 : {}개 '.format(o_no,o_contents,o_qty))


# 방법 5 f 포맷

print('주문번호 : {}번'.format(o_no))
print(f'주문번호 : {o_no}번')

# python grammar2 51page
# %주민번호 앞자리  %6d -> 숫자크기만큼 자리 확보 %d <- 오른쪽 정렬
print('%d'%100)
print('%6d'%100)

# %s -> 자리차지 %숫자s
print('%s'%'java')
print('%8s' %'java')
print('%8s %8s' %('java','python'))
print('%-8s %-8s' %('java','python')) # 음수 -> 왼쪽 정렬
print('%8s %8s' %('c','c'))
print('%8s %8s' %('c','c++'))


# 53page

# 파이썬표준 입출력 간단 > 오른쪽 < 왼쪽 + *

# >10 : 숫자만큼 자리확보, 오른쪽 정렬
# : <- 콜론
num = 100
print('%10s'%num)
print('{0:>10}'.format(num))   # 10자리확보 오른쪽 정렬
print('{0:>+10}'.format(num))  # + 기호표시(=양수 표시)
print('{0:*<+10}'.format(num)) # *로 채우기 숫자수정 방지 위해 사용 +100******
print('{0:*>10}'.format(num))

# 숫자 천단위 표시
tot = 12000000
print('{0:,}'.format(tot))

# 소수점이하 자릿수 -> 자릿수f
rate = 1/3
print('{}'.format(rate))
print('{0:.2f}'.format(rate)) # 소수점이하 2자리

# 0으로 채우기 zfill()

print('1'.zfill(5)) # 1 -> 00001
print('100'.zfill(5)) #100 -> 00100

# range(5) -> 범위 : 5 -> 인덱스 0,1,2,3,4
# range(시작값, 마지막+1) -> range(1,6) -> 1,2,3,4,5
# range(시작값, 마지막+1,간격) range(1,10,2) -> 1,3,5,7,9

# 반복문
'''
for 변수 in range() :
    print(변수)

'''
for 변수 in range(5) :  # 0~4
    print(변수)

#1~100까지
# zfill() 문자로 처리
for 변수 in range(1,101) :  # 0~4
    print(str(변수).zfill(3))
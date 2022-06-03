# 문자열에서 공백지우기 strip() , left -> lstrip() , right -> rstrip()
'''
  데이터
↑        ↑
왼쪽     오른쪽
lstrip('데이터') # 왼쪽 데이터 지우기
rstrip('데이터') # 오른쪽 데이터 지우기

'''


# .포인터연산자
# data.lstrip()
# data.rstrip()

# data.lstrip()
data = '                       데이터'
print(data)
print()
공백지운후변수 = data.lstrip() # 왼쪽 공백을 지운 후 변수에 저장
print(공백지운후변수)

# data.rstrip()
data = '                       데이터              '
print(data)
print()
공백지운후변수 = data.rstrip() # 오른쪽 공백을 지운 후 변수에 저장
print(공백지운후변수)

# 데이터 영문 대문자, 소문자 산재
# Python, PYTHON, python

항목변수 = 'PYTHON'
print(항목변수)  # PYTHON

# 영소문자 전환 lower() --> 변수.lower()
항목변수 = 'PYTHON'
항목변수 = 항목변수.lower()
print(항목변수)  # python

# 영대문자 변화 upper() --> 변수.upper()
항목변수 = 'python'
항목변수 = 항목변수.upper()
print(항목변수)  # python

# 첫문자 대문자로 변환 함수
data = 'python' # -> Python
data = data.capitalize()
print(data)

# slicing 문자열 자르기
'''
ace         <- 문자열
012         <- index number
[숫자]      <- 위치 0부터 시작, 뒤에서 부터 -숫자(시작:-1 ~) 
[ : ]       <- 처음부터 끝까지, 대괄호 사용
[시작:]     <- 시작부터 끝까지
* [:끝]     <- 처음부터 끝에서 -1번까지 ex) [:5] >문자열 5번째까지 나옴_0부터 생각 시 문자 6개가 나와야된다고 하지만 걍 1부터 계산한다고 생각하기
abracadabra <- 문자열
01234567890 <- index number


'''
data = 'ace'
data[0]
print(data[0])  # a
print(data[2])  # e
print(data[-1]) # e
print(data[:])  #    처음부터 끝까지
print(data[0:2])  # ac 처음부터 3-1 까지 나옴
print(data[:2]) 

data = 'abracadabra'
print(data[:2])
print(data[7:])

'''
'첫둘셋넷다여일'
'''
s = '첫둘셋넷다여일'
# 첫둘셋
s=s[0:3]
print(s)

# 첫둘셋넷다여
s=s[:6]
print(s)

# 셋넷
s=s[2:4]
print(s)
'''중간고사'''
# jnu = '제주대학교'

# 1. 제주
# 2. 대학교
# 3. 대학 

# jnu = '제주대학교'
'''방법 1
print(jnu[0:2])
print(jnu[2:])
print(jnu[2:4])
'''
'''방법 2_얘는 따로 따로  하기
jnu=jnu[0:2]
print(jnu)
jnu=jnu[2:]
print(jnu)
jnu=jnu[2:4]
print(jnu)
'''
'''방법 2 _ 연속해서 하기
a,b,c=jnu[0:2],jnu[2:],jnu[2:4]
print(a,b,c)
'''

s= '1234567'
s=s[0:3]
print(s)

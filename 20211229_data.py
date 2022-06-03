# 실습문제
# 버스 정류소
# 365번 버스가 잠시 후 도착합니다
# 336번 버스가 잠시 후 도착합니다
# 270번 버스가 잠시 후 도착합니다

# 변수의 사용
busNumber1, a = '270번', '336번' # 문자열
# comma(,) 로 구분
print(busNumber1, a, '버스가 잠시 후 도착합니다')  # 문자열 '' or " "

# 문자열 합치기 +
'''
comma
구분, 서로 다른 성질의 데이터도 무난하게 출력

+
타입이(=성질)이 같아야 한다.
'''
a = "pyt"
b = "hon"
print(a,b) # 콤마 한칸 띄기, 구분

busNumber = 270 # 숫자
print(busNumber, '번 버스가 잠시 후 도착합니다') 

# 문자열합치기 + 사용

print(3+4)
print('파이'+"썬") # 문자열 합치기 , type이 일치해야 함
# type error A
# busNumber = 270 # 숫자 int, integer; 정수  해결책 -> 숫자 자체에 ' ' 씌우기
# print(busNumber + '번 버스가 잠시 후 도착합니다') # str, string; 문자열 #  'type errorA'

# 방법 1 숫자를 문자로 변경 ' ' or " "
busNumber = '270' # 숫자 int, integer; 정수  해결책 -> 숫자 자체에 ' ' 씌우기
print(busNumber + '번 버스가 잠시 후 도착합니다') # str, string; 문자열 # 보기에는 에러가 없으나 터미널에서 에러가 발생한다. 'type errorA'
# 기능, 함수 print( ) 함수의 기본형태 -> 함수이름() ex) int(), str() 도 함수이다
'''
casting
 int() --> 정수형으로 타입 변경 의미
 str() --> 문자열로 타입 변경 의미
'''
# 방법 2 처리할 때 type 변경
busNumber = '270' # 숫자 int, integer; 정수  해결책 -> 숫자 자체에 ' ' 씌우기
print(str(busNumber) + '번 버스가 잠시 후 도착합니다') # str, string; 문자열 # 터미널에서 에러가 발생한다. 'type errorA' # 해결책 -> Print안의 busNumber에 str() 씌운다.

# 코로나 관련 기사를 인공지능을 이용해서 작성
month = 25
virus = '코로나'
nation = '대한민국'
print(virus,'가', month, "개월째 전세계를 뒤흔들고 있습니다.")                   # print("코로나가 15개월째 전세계를 뒤흔들고 있습니다.")-개월수가 변할 수 있으므로
print(nation,'은', virus,"로 부터 안전해지기 위해 최대한 노력을 하고 있습니다.") # print("대한민국은 코로나로 부터 안전해지기 위해 최대한 노력을 하고 있습니다.")
print(nation,'에서', virus,"를 물리쳐내기 위해 함께 노력 하시겠습니까?")         # print("대한민국에서 코로나를 물리쳐내기 위해 함께 노력 하시겠습니까?")

''' print 함수 사용시 변수를 지정한 것들은 ex) month, virus 문자로 생겨도 따로 '' or " " 표시로 묶어주지 않는다
    그리고 함수가 끝나고 문자를 쓰고 함수가 시작 될 때는 항상 , or + 를 까먹으면 안된다.
'''

# 코로나 관련 기사를 인공지능을 이용해서 작성 ## 방법 2 문자열 합치기 +
month = 25
virus = '코로나'
nation = '대한민국'
# print(virus,'가', month, "개월째 전세계를 뒤흔들고 있습니다.")                   
print(virus+'가', str(month)+"개월째 전세계를 뒤흔들고 있습니다.") or print(virus+'가 ' +str(month)+"개월째 전세계를 뒤흔들고 있습니다") # -> , 대신 띄어쓰기 사용
# print(nation,'은', virus,"로 부터 안전해지기 위해 최대한 노력을 하고 있습니다.") 
print(nation+'은', virus+"로 부터 안전해지기 위해 최대한 노력을 하고 있습니다.")
# print(nation,'에서', virus,"를 물리쳐내기 위해 함께 노력 하시겠습니까?")       
print(nation+'에서', virus+"를 물리쳐내기 위해 함께 노력 하시겠습니까?") 


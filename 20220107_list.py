# list 확장 extend()

pack1 = ['lemon','melon','banana'] # 리스트1
pack2 = ['apple','watermelon']     # 리스트2
합친리스트 = pack1 + pack2         # 컴퓨터의 메모리 : pack1, pack2, 합친리스트 > 비효율적으로 많이 사용하게 된다.
print(합친리스트)

pack1 = pack1 + pack2       # 메모리를 1개로 사용한 것
print(pack1)
pack1 += pack2              # 코드 축약
print(pack1)
pack1.extend(pack2)         # 코드 축약을 수식이 아닌 .extend로 표시
print(pack1)


f='lemon','melon','banana' # 튜플(tuple) == ('lemon','melon','banana')
print(f, type(f)) 
# 구분하기 위한 콤마(,)의 출력
print('lemon','melon','banana')     # print 내의 , 는 표시가 되지 않는다 = 띄어쓰기로 나타남
print()
print('lemon','melon','banana' ,sep=',')  # filename.csv  공통적인 데이터 포맷  *csv; c콤마로 s(=sep)구분된 v값


# print() <- 한 줄에 출력
print(1)
print('a')
print('부산')
print()
# print(, end=') <- 같은 행에 출력
print(1,end='')
print('a',end='')
print('부산',end='')
print()
# print(, end=') <- 같은 행에 출력_ 너무 붙어 있어서 한칸 띄우고 싶을 때
print(1,end=' ')
print('a',end=' ')
print('부산',end=' ')

# 파이썬 grammer 4. 18p_기말고사
year = 2021
month = 12
day = 24
hour = 10
minute = 20
second = 30

print(year, month, day, sep='/', end=' ')
print(hour, minute, second, sep=':')


# 심심해서 한 것
year = input('년도 : ')
month = input('월 : ')
day = input('일 : ')
print('태어난 시기 :', end=' ')
print(year,month,day, sep='/')


# 정렬하여 출력 rjust 오른쪽 정렬 >, ljust 왼쪽정렬 <
# 문자를 다루는 함수이다

s = 'aaa'
n = 11      
print(s)
print(n)
print()

s = 'aaa'
n = 11                           # 현재 숫자 > 문자로 변경 '11'or str(n)
print(s.rjust(10), end='|')      # 큰 길이(칸) 10, 오른쪽 >
print(s.ljust(10), end='|')      # 큰 길이(칸) 10, 왼쪽 <
print(str(n).rjust(10), end='|') # 큰 길이(칸) 10, 오른쪽 >
print(str(n).ljust(10), end='|') # 큰 길이(칸) 10, 왼쪽 <



n =[3,6,9,4,2,6,7,9,32]
print(n)  # [3,6,9,4,2,6,7,9,32]
print()
n.sort()             # 작은 것 > 큰 순으로 정렬 = 오름차순정렬
print(n)

print('*'*20)        # 그냥 구분선

n.sort(reverse=True) # 내림차순 정렬
print(n)

f = ['lemon','melon','banana']

# 문자열 -> 데이터 사용을 위한 리스트 split()
s = '교수님 화면 전환 해야 되요. 교수님 화면 안보입니다!'    # 연설문
print(s, type(s))           # str type 이지만
print(s.split(), type(s))   # list로 해서 띄어쓰기로 따라서 구분을 해 준다.

# 실습 count('화면')
print(s.split().count('화면'))
print(s.count('화면'))
print(s.find('화면'))





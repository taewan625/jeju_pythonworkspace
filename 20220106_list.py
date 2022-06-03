# list
'''
리스트변수 = [1,2,3,4,5] # 리스트는 [ ] 사용
리스트변수 = ['aaa','bbb','ccc']
'''


dept = ['국문과','영문과','일문과','중문과']
# 인덱스 : 변수명[위치] # 0부터 시작
# dept[2]  # 일문과를 뽑고 싶을 때
# print(dept[2])
from random import*
# random.random()
# 0 ~ 3 : 0,1,2,3
# 기말고사
dept = ['국문과','영문과','일문과','중문과']
from random import*
a = dept[randrange(1,4)]
print(a)

# slicing
dept = ['국문과','영문과','일문과','중문과']
print(dept[:2]) # [0] [1]

# # del 삭제
# a = 1
# print(a)
# del a
# print(a)
dept = ['국문과','영문과','일문과','중문과']
del dept[0]
print(dept)

# 요소 뒤 추가 .append()
dept.append('국문과')
print(dept)         # 맨 끝으로 들어와짐

# sort()  작 ~ 큰순으로 정렬 하기 = 오름차순
a = [3,6,2,3,56,8]
print(a)
a.sort()
print(a)

# reverse()내림차순으로 정렬   # 숫자 문자 상관없이 다 됨
a.reverse()
print(a)

# 중간 끼워 넣기 , 삽입 insert()
dept = ['국문과','영문과','일문과','중문과']
dept.insert(1,'수생') # insert(인덱스 위치, 추가할 값 첨가)
print(dept)

# 요소 삭제 remove(값)  # 인덱스 위치 X
dept.remove('일문과')  # remove는 값을 지우는 것이다
print(dept)

# pop() 뒤 요소부터 차례로 꺼내기
dept = ['국문과','영문과','일문과','중문과']
print(dept)
dept.pop()
print(dept)
dept.pop()
print(dept)
dept.pop()
print(dept)
dept.pop()
print(dept)

# count()
dept = ['국문과','영문과','일문과','중문과','수생','국문과','영문과','일문과','중문과','수생','국문과','영문과','일문과','중문과','수생','국문과','영문과','일문과','중문과','수생','국문과','영문과','일문과','중문과','수생']
dept.count('수생')
print(dept.count('수생'))   # 데이터가 리스트에 5개가 있다를 보여준다
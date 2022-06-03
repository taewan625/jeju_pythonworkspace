# 라이브러리 사용 import

print(round(2.54)) # 내장함수

# floor() # 주황 밑줄은 문제가 있음을 의미
# import 방법 1
# from 라이브러리 이름 import *
from math import *
from random import * # 실무에서 사용할 때 이렇게 같이 붙임
# floor # 주황 밑줄이 사라짐!

# 버림 floor()
print(floor(3.99))

# 올림 ceil()
print(ceil(3.0001))

# 제곱근 sqrt()
print(sqrt(4))


# random 라이브러리
from random import * # 이건 연습이라 이런데 원래는 라이브러리끼리 같이 붙여준다
r = random() # 0.0 ~ 1.0 미만
print(r)
# 1 ~ 45 이하
lot = randint(1, 45) # 1~ 15이하 랜덤 출력
print(lot)

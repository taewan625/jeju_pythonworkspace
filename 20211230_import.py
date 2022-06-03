# import 외부 라이브러리 사용할 때 

# 방법 1 : from 라이브러리 이름 import * 사용이전 이 내용이 선언되어야 한다.

# 값 올림 ceil()
print(round(3.4)) # 내장함수
from math import *
print(ceil(3.1)) # import math

# 방법 2 : import 라이브러리 이름
# 사용 : 라이브러리이름. 함수()
#                      ↑ 포인트 연산자
# 값 내림 floor()
import math 
print(math. floor(3.9))


# turtle library
# 터틀그래픽 <- Graphic User Interface (GUI) tkinter
import turtle # 먼저 정의 import 방법 2 , 라이브러리 파일 -> module
# 도화지 생성

# 정사각형
t = turtle.Turtle() # Turtle class
t.shape("turtle")    # t 변수, 생성자, instance 도화지
t.speed('slowest')   # 속도 조절
angle=90
dist=100
t.forward(100)       # pixel
t. left(90)          # angle 90 직각 120 삼각
t.forward(100)
t. left(90)
t.forward(100)
t. left(90)
t.forward(100)
turtle.mainloop()    # loop; 화면이 계속 유지

# 정삼각형
t = turtle. Turtle() # Turtle class
t.shape("turtle")    # t 변수, 생성자, instance 도화지
t.speed('slowest')   # 속도 조절
angle=120
dist=80
t.forward(dist)      # pixel
t. left(angle)       # angle 90 직각 120 삼각
t.forward(dist)
t. left(angle)
t.forward(dist)
t. left(angle)
turtle.mainloop()    # loop; 화면이 계속 유지

# 육각형
t = turtle. Turtle() # Turtle class
t.shape("turtle")    # t 변수, 생성자, instance 도화지
t.speed('slowest')   # 속도 조절
angle=60
dist=80
t.forward(dist)      # pixel
t. left(angle)       # angle 90 직각 120 삼각
t.forward(dist)
t. left(angle)
t.forward(dist)
t. left(angle)
t.forward(dist)      # pixel
t. left(angle)       # angle 90 직각 120 삼각
t.forward(dist)
t. left(angle)
t.forward(dist)
t. left(angle)
turtle.mainloop()    # loop; 화면이 계속 유지

# 원
t = turtle. Turtle() # Turtle class
t.shape("turtle")    # t 변수, 생성자, instance 도화지
t.speed('slowest')   # 속도 조절
t.circle(1200)       # 크기
turtle.mainloop()
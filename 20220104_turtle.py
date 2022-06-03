# for 문 활용 turtle graphic

import turtle as t  # 별명 t로 turtle 모듈 사용
n = 50 # 초기값
t.shape('turtle')
t.speed('fastest')

# 원패턴
for i in range(n):  # i = 반복변수
    t.circle(120)
    t.right(360/n)
t.mainloop()

##
import turtle as t  # 별명 t로 turtle 모듈 사용
n = 50 # 초기값
t.shape('turtle')
t.speed('fastest')

angle = 120
for i in range(300):  # i = 반복변수 / 300이란 각도를 줘서 일정한 패턴을 주는 것
    t.forward(i)
    t.right(angle)
t.mainloop()
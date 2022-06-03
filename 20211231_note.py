# 변수 = 1000
# print(변수) # 내장
# 변수 = 2+4
# 변수 = '문자 두번째 문자'
# 변수 = input()
# import turtle # 그림
# 변수 = turtle.Turtle() # 외장

# # import 방법 1
# import tkinter
# 변수 = tkinter.Tk()  # class 객체, 붕어빵 틀
# 변수.mainloop()

# from tkinter import *  # 방법 2
from tkinter import *    # 프로그램
변수 = Tk()  # from을 사용하면 변수 = tkinter.Tk() 의 tkinter 를 생략할 수 있다x
변수.title('이게 돼?')
변수.geometry("720x480")
Label = Label(변수, text= "항목을 입력하세요")
Label.pack()
변수.mainloop()
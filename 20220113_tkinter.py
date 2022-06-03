# tkinter
'''
tkinter
윈도우 : 버튼, 텍스트박스, 레이블, 체크박스, 라디오버튼, ..........
활용   : 프로그램도 만들 수 있다.
키오스크~
영화관
'''
# import

from tkinter import*
root =Tk() # root라고 하는 건 맨 바닥층에 있다고 그냥 표시한 것. 변수이므로 아무거나 써도 됨. 이제 이 위에 여러가지 쌓는다는 의미

# 버튼도 만들고 -> 이것만 있는 걸 class로 묶어놔서 편리하게 쓰는 것
# 내용도 만들고
# 입력도 하고
root.title('제주대학교 권태완')
root.geometry("720x480+500+300")
# 레이블 만들기
label = Label(root,text='북카페 회원 전용 관리프로그램이다') # Label이란 class 안에 들어갈 text를 쓰고 싶을 때 
label.pack()    # ↑ 이것만 있으면 안나옴. tkinter은 f 처럼 open 후 close 하듯이 pack 으로 마무리 지어야 함
# 버튼 만들기
bt1 = Button(root, text='버튼누르기1')
bt1.pack()
bt2 = Button(root, text='버튼누르기2', width = 20, height=5)
bt2.pack()
bt3 = Button(root, text='버튼누르기3', width = 20, height=5, fg='blue')
bt3.pack()
# 버튼 명령 command = 
bt4 = Button(root, text='버튼누르기4', width = 20, height=5, fg='blue', command=exit)  # exit는 함수가 아니여서  뒤에 () 안붙임
bt4.pack()
def 실행할함수():
    print("실행함수버튼 동작")

bt5 = Button(root, text='함수실행', width = 20, height=5, fg='blue', command=실행할함수)
bt5.pack()

# 한줄 입력 칸
e = Entry(root, width=50)
e.pack()

# 여러 줄 입력
txt = Text(root, width=50, height=5)
txt.pack()

# 마무리
Tk().mainloop()
# python Grammer-15-thinter 실행파일 만들기


from tkinter import*
root =Tk()
root.title('제주대학교 권태완')
root.geometry("720x480+500+300")
label = Label(root,text='북카페 회원 전용 관리프로그램이다')
label.pack()
bt1 = Button(root, text='버튼누르기1')
bt1.pack()
bt2 = Button(root, text='버튼누르기2', width = 20, height=5)
bt2.pack()
bt3 = Button(root, text='버튼누르기3', width = 20, height=5, fg='blue')
bt3.pack()
bt4 = Button(root, text='버튼누르기4', width = 20, height=5, fg='blue', command=exit)
bt4.pack()
def 실행할함수():
    print("실행함수버튼 동작")
bt5 = Button(root, text='함수실행', width = 20, height=5, fg='blue', command=실행할함수)
bt5.pack()
e = Entry(root, width=50)
e.pack()
txt = Text(root, width=50, height=5)
txt.pack()
Tk().mainloop()
# 파일 읽기 : covid.txt, 모드 r

# f = open('covid.txt','r', encoding='utf8') # utf8 포맷의 파일 covid.txt 를 읽기
# print(f.read())     #  읽기
# f.close()           # 파일 사용 후 닫기

# 파일 읽기 : readline(), covid.txt, 모드 r
f = open('covid.txt','r', encoding='utf8') # utf8 포맷의 파일 covid.txt 를 읽기
print(f.readline())     #  줄 단위 읽기
f.close()           # 파일 사용 후 닫기

# 여러줄 읽고 싶을 때 -> print() 때문에 공백이 생김
f = open('covid.txt','r', encoding='utf8') # utf8 포맷의 파일 covid.txt 를 읽기
print(f.readline())     #  줄 단위 읽기
print(f.readline())     #  줄 단위 읽기
print(f.readline())     #  줄 단위 읽기
print(f.readline())     #  줄 단위 읽기
f.close()           # 파일 사용 후 닫기

# 공백 해결
f = open('covid.txt','r', encoding='utf8') # utf8 포맷의 파일 covid.txt 를 읽기
print(f.readline(), end='')     #  줄 단위 읽기
print(f.readline())     #  줄 단위 읽기
print(f.readline(), end='')     #  줄 단위 읽기
print(f.readline())     #  줄 단위 읽기
f.close()           # 파일 사용 후 닫기


# 줄이 몇개인지 어떵 아냐! -> 반복 읽기
f = open('covid.txt','r', encoding='utf8')
# print(f.readline())
while True : # While; 참일 동안 계속 반복해서 읽음
    # 마지막 줄까지만 읽고
    # 만약에 마지막 줄이면 탈출해 = 반복하지마 = 반복에서 나와
    line = f.readline()         # 라인을 계속해서 읽는데
    if not line :               # 없으면 빠져나오는 것을 의미
        break
    print(line, end='')        # 줄단위 간격읽기
f.close()           # 파일 사용 후 닫기
# same
f = open('covid.txt','r', encoding='utf8')
while True :
    line = f.readline()         # 라인을 계속해서 읽는데
    if not line :               # 없으면 빠져나오는 것을 의미
        break
    print(line, end='')        # 줄단위 간격읽기
f.close()


# readlines() --> 읽기 --> 리스트 형태 ['미국 : 61,158,120' ,'인도 : 35,753,572' , , , ]
# lines 에 s를 붙여서 for문을 이용해서 여러줄 나오게 하는 방법
f = open('covid.txt','r', encoding='utf8')
lines = f.readlines()       # line -> lines / f.readline-> f.readlines
# 반복 읽기
for i in lines : # 위에 리스테 있는게 i로 들어가서      # lines
    print(i, end='') # print 하는 것
f.close()


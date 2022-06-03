# 파일 생성
'''
open("생성할파일이름.확장자","모드") 
# 모드 w : 쓰기, 생성, 덮어쓰기
       a : 기존 파일 내용에 추가
       r : 파일내용 읽기
open("sample.txt","w") # 현재 작업 공간에 sample.txt 파일을 쓰기모드로 생성
수행할 내용 --> 파일내용 작성
open("sample.txt","a") # sample.txt 파일에 내용을 추가 의미
close()
수행할 내용 --> 파일내용 작성
close()
open("sample.txt","w") # sample.txt 파일의 내용을 읽기
수행할 내용 --> 파일내용 읽기
close()
'''

# 한글작성
from os import write #?? 뭐지 ??

f = open("sample.txt","w",encoding="UTF8")                 # 파일 객체
f.write('1. 한글이 깨짐-> encoding="UTF8" 로 이제 안 깨짐  ')   # str만 가능함. 에러가 뜸. '이 안에 다 써야함'
f.close()

# mode = a 내용 추가_1 (다음 줄 추가)
f = open("sample.txt","a",encoding="UTF8")              
f.write('2. "a"를 넣으면 기존 내용의 뒷부분에 내용이 추가 된다')   
f.close()

# mode = a 내용 추가2 (다음 행 추가)
f = open("sample.txt","a",encoding="UTF8")              
f.write('\n3. "\\ n" 을 이용하여서 다음 행에 추가')   # 역슬래쉬 2개를 써야 출력될 때 1가 나옴
f.close()


## 덮어쓰기 연습
f = open("sample2.txt","w",encoding="UTF8")
f.write('1. 파이썬\n')
f.write('2. 파이\n')
f.write('3. 파\n')
f.close()

f = open("sample2.txt","w",encoding="UTF8")  # 내용이 덮어 써짐
for i in range(1,6) : 
    f.write('{}. 번 줄입니다\n'.format(i))
f.close()

# 저장, 읽기 파일위치 --> 경로 path
# 경로/파일이름                    or       경로\\파일이름
# C:/pythonworkspace/파일이름      or     # C:\\pythonworkspace\\파일이름

f = open("sample2.txt","w",encoding="UTF8")

# print는 파일에 영항을 주지 않는다. 그냥 평상시 하던 print
f = open("sample2.txt","a",encoding="UTF8")
print('1번 줄입니다')
print()
print('2번 줄입니다')
f.close()

'''
1 번줄입니다

다음줄입니다
'''
# 파일에 영향을 주는 print 함수
f = open("sample2.txt","a",encoding="UTF8")
print('1번 줄입니다', file=f)
print(file=f)
print('2번 줄입니다', file=f)
f.close()
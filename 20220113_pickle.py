# pickle file 생성, binary 형태
# 1. 설명
# 저장 dump()

# 2. 모듈 사용 import
'''
import pickle
import random -> from  random import *
import os       # 운영체제 명령
import 라이브러리
import 모듈
'''
# f 파일
f = open('피클파일.pk1','wb') # 이 파일은 핸들링 하기 위해 f 사용
ranking = {'1위' : ['서복', '4,5만'],
           '2위' : ['귀멸의 칼날' '5천'],
           '3위' : ['노바디', '4천'],
}
print(ranking, type(ranking))
f.close()

# 실습 문제_2위 데이타 추출 하세요
f = open('피클파일.pk1','wb') # 이 파일은 핸들링 하기 위해 f 사용
ranking = {'1위' : ['서복', '4,5만'],
           '2위' : ['귀멸의 칼날' '5천'],
           '3위' : ['노바디', '4천'],
}
print(ranking['2위'])           #{}가 dictionary기 때문에 print 시 dictionary 방식으로 출력을 해야함
f.close()

# dump -> 2진법으로 나타내는 것이므로 (0,1)조합이므로 txt 문서와 달리 파일은 존재하는데 내용이 안나옴
import pickle
f = open('피클파일.pk1','wb') # 이 파일은 핸들링 하기 위해 f 사용
ranking = {'1위' : ['서복', '4,5만'],
           '2위' : ['귀멸의 칼날' '5천'],
           '3위' : ['노바디', '4천'],
}
pickle.dump(ranking, f)        # dump=return 값은 없어요= 우리가 보는 문자 형식으로 안보임.라고 ranking에 뜸 그러면 내용 받고 그냥 끝
f.close()


# 읽기 load() 모드 rb
from pickle import *

f = open('피클파일.pk1','rb') # 이 파일은 위에서 binary data로 읽지 못했다
binary_date  = load(f)        #load = 파일을 열어라(f)f라는 파일을 열겠다-어떤 형식으로든지 나타내겠다 -> 바이너리 데이타도(어떤 형식도 된다니깐) 출력해줌
print(binary_date, type(binary_date))
f.close()

# dump, load, read 차이점
'''
dump, load는 function이다.
read-class 안에 있는 함수인 method 이다.
'''
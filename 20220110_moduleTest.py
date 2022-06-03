# 모듈 호출() : import 파일이름 (); 괄호는 사용을 의미
'''
# random 에 있는 무엇을 쓰겠다는 의미
import random
random.
# import 에 있는 무엇을 쓰겠다는 의미
import turtle
turtle.



'''

# import module_main      # 모듈을 사용 하기 위해 import 한 것
# module_main.moduleSample()

# import turtle
# turtle.

# 대리점 기능 부여, 모듈 활용
# 대리점 회원 -> 본점 회원
# 대리점 -> 회원가입 대리점, 본점 db 

# import module_main as mm # as ** ; 이름이 너무 길어서 mm 으로 쓰겠음 의미
# mm.member_reg()
# mm.regMember('A대리점')


# 1. 모듈사용을 위한 import
import dbmanange as db

# 2. 모듈에 있는 기능 호출
db.dbcom('a123','b321')

# 3. 상품목록 가져오기
db.dblist('dept')

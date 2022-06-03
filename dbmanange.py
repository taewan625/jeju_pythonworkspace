# module file : dbmanange.py
# module name : dbmanange

'''
1. db 연결 : id, pw
2. db 목록 보기
3. record 상세히 보기
4. data 수정
5. 레코드 삭제

1) DB구조(스키마, schma)
   번호, 이름, 학과, 학번, 등등
2) 레코드
   1번, 권태완, 수생, 2016106033
   2번, 권태완, 수생, 2016106033
   3번, 권태완, 수생, 2016106033
   4번, 권태완, 수생, 2016106033
   5번, 권태완, 수생, 2016106033
   6번, 권태완, 수생, 2016106033
   .
   .
   .
   .

3)필드명 : 이름, 학과


'''

# 1. db 연결 : id,pw
def dbcom(id,pw):
    # id, pw 를 통해서 사용자가 있는지
    print('등록된 사용자입니다, 연결성공')
# 2. db 목록 보기 : 해당 데이타베이스
def dbselect(dbname) :  # grammer 5 7p dbselect 같은 것
    # select ~~~ 쿼리문
    print(dbname, '목록보여주기')
    print('1번, 권태완, 수생, 2016106033')
# 3.
def recdelete(recno): # 원하는 부분만 지울 때 레코드를 번호로 해서 번호를 지우는게 편리
   # delet from ~~~ 번호 = recono : 쿼리문
   print('{} 번 레코드가 삭제되었습니다.'.format(recno))

# 4. 기능 생성 -> 수정
   # def dbupdate(dbconn):
      # print('{}번 레코드가 수정되었습니다.'.format(dbconn))
def datamodi(field, contents) :
   print('{}의 내용을 {}로 변경합니다'.format(field, contents))
# 5. 
def recdetail(recno):
   print('{}번 레코드 상세표시'.format(recno))
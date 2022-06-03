# covid-19 누적확진자 데이터 파일 만들기

'''
파일이름 : covid.txt

미국 : 61,158,120
인도 : 35,753,572

러시아 : 10,485,705
영국 : 14,651,4472

'''
# 파일만들기 covid.txt ,모드 : w(write), encoding='utf8' '한글'
f = open('covid.txt','w', encoding='utf8') # utf8 포맷의 파일 covid.txt 를 생성
print('미국 : 61,158,120', file=f)                  # print()를 이용하는 방법은 기본적으로 한 줄씩 사용 하는 것
print('인도 : 35,753,572', file=f)                  # 알아서 다음 줄로 넘어감
f.close() # 파일 사용 후 닫기

# 파일내용 추가하기, 모드 : a, encoding='utf=8'
f = open('covid.txt','a', encoding='utf8')
f.write('러시아 : 10,485,705\n')                    # f.write는 \n 으로 다음 행 넘기기를 사용
f.write('영국 : 14,651,4472')
f.close()

'''
[실습]
월별 상품 재고 리스트 현황
파일 만들기 : monthly.txt
내용
1월 재고량
상품명 입고량 판매량 재고
'''

# 파일 만들기
f = open('monthly.txt','w', encoding='utf8')
#내용
f.write('1월 재고량\n')
f.write('상품명 입고량 판매량 재고')
f.close()


# 파일이름 코딩을 통해서 만들기
'''
1월 재고량.txt
2월 재고량.txt
3월 재고량.txt
.
.
12월 재고량.txt
'''

month = '1월' # 변수, 어디에서든지 사용가능함
f = open(month+' 재고량.txt','w', encoding='utf8')
#내용
f.write(month+' 재고량\n')
f.write('상품명 입고량 판매량 재고')
f.close()

month = 4 # 숫자변수  -> '4'+ or str(4)+ 만 가능 , comma는 에러가 뜬다 
# 문자+문자 (o)
# str(숫자)+문자 (o) casting
f = open(str(month)+'월 재고량.txt','w', encoding='utf8')
#내용
f.write(str(month)+'재고량\n')
f.write('상품명 입고량 판매량 재고')
f.close()


## 파일 여러개 동시에 만들기
# 파일 1월~12월_range
for month in range(1,13):
    f = open(str(month)+'월 재고량.txt','w', encoding='utf8')
    f.write(str(month)+'재고량\n')              # f.write를 for과 같은 단으로 내리면 1월~12월까지 
    f.write('상품명 입고량 판매량 재고')        # 파일은 나오지만 내용은 나오지 않게 된다.
f.close()

# 파일 1월~12월_lsit
month = [1,2,3,4,5,6,7,8,9,10,11,12]
for i in month:
    f = open(str(i)+'월 재고량.txt','w',encoding='utf8')
    print(str(i)+'월 재고량',file=f)
    print('상품명 입고량 판매량 재고',file=f)
f.close()


# 1월 일자별 재고량 파일
# 1월 1일~31일 : 31개 파일 만들기
'''
1월 1일 재고량.txt
1월 2일 재고량.txt
.
.
.
1월 31일 재고량.txt
내용
1월7일 재고량
상품명 입고량 판매량 재고
'''
month = '1월'        # 전역변수 : 파일 내 어디서든 활용 _ 고정된 변수
daily = range(1,32)  # 멤버변수 : 해당 사용 구역(함수, 반복문..)_ for과 같이 함수를 통해서 변하는 변수

# 실습 내용
# 내 풀이
month = '1월'
for daily in range(1,32):  # for i in daily
    f = open(month+str(daily)+' 일 재고량.txt','w', encoding='utf8')
    f.write(month+str(daily)+'재고량\n')  
    f.write('상품명 입고량 판매량 재고')  
f.close()

# 다른 풀이
month = '1월'
daily = range(1,32)
for i in daily:
    f = open('{} {}일 재고량.txt'.format(month, i),'w', encoding='utf8')
    print('{} {}일 재고량'.format(month, i), file=f)
    print('상품명 입고량 판매량 재고', file=f)
f.close()


# csv 파일 comma, -> 다른 응용프로그램 db 활용
# csv로 변경 후 utf8로만 이용하면 한글은 깨지게 된다. - 외국 프로그램은 깨지고 한국 프로그램은 안깨짐
month = '1월'
daily = range(1,32)
for i in daily:
    f = open('{} {}일 재고량.csv'.format(month, i),'w', encoding='utf8')
    print('{} {}일 재고량'.format(month, i), file=f)
    print('상품명 입고량 판매량 재고', file=f)                 # 컴마를 안하면 엑셀 파일에 연결되서 쓰여지고 컴마 하면 셀마다 하나씩 들어가짐
f.close()
# 해결 utf-8-sig
month = '1월'
daily = range(1,32)
for i in daily:
    f = open('{} {}일 재고량.csv'.format(month, i),'w', encoding='utf-8-sig') ##
    print('{} {}일 재고량'.format(month, i), file=f)
    print('상품명,입고량,판매량,재고', file=f)                 # comma, -> 다른 응용프로그램 db 활용
f.close()
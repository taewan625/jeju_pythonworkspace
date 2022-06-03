# with 키워드를 활용한 파일 만들기
# close() 필요 없음

# f
f = open('without_with.txt','w',encoding='utf8')
print('123','abc', file=f) # print()는 print('','','') 가능하다
f.write('321,cba') # *args가 write에는 없다 print 와 달리 str만 넣을 수 있다. ex) f.write('a','b','c') 처럼 컴마로 구분해서 못넣음!!! cf) print는 가능
f.close()

# with
with open('without_with.txt','w',encoding='utf8') as f:
    print('123,abc', file=f)
    f.write("'321','cba'")  # 문장안에서 '' '' 로 구분하는 방법
f.close()

# break 반복문 탈출
'''
커피자판기
커피재료 수량

커피제공
커피 - 1

커피재료 소진되면
    커피제공 중지
    break
'''
coffee = 1000 # 정의, 초기화, 속성
while True : 
    print('커피제공')
    coffee-= 1          # 무한루프 ctrl +c
    print(coffee, '개 남았습니다.')
    if coffee ==0 : 
        print('재료 소진')    # 커피가 마감 되었음을 알려주고 싶어서 if문 안에 print 쓰기
        break                 # if 에서 커피가 0 일 때 break 시킴
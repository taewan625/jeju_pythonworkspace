# pass 조건문 안에서 아무 것도 수행 하지 않게 하려면

'''
식품점에 특정과일이 없을 경우 구매요청 하고 싶을 때

과일리스트 = ['a','b','c','d']
특정과일 = 'b'

만약에 특정과일이 과일 리스트에 있다면
pass
없다면 
구매 요청을 한다
'''

f_list = ["lemon","melon","banana"]
o_item = "melons"
if o_item in f_list:
    pass
else :
    print(o_item, '구매 요청을 한다')

과일리스트 = ["lemon","melon","banana"]
특정과일 = 'lemon', 'liwi'
if 특정과일 in 과일리스트:
    pass
else : 
    print(특정과일,'구매 요청을 한다' )


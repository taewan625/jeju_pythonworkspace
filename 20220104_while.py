# while 반복문
'''
형식
while 조건 : # 참이면 반복
    수행문1
    수행문2
'''
# hit = 0
# while True :        # 무한 반복  / 멈추기 Ctrl + c
#     hit = hit + 1   # = (hit += 1) 
#     print('참이면 %d 번째실행됩니다'%hit)

hit = 0
while hit < 100 :       # 참인 동안 반복
    hit += 1 
    print('나무를 {} 번째 찍었습니다'.format(hit))

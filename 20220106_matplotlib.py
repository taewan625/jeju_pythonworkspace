# matplotlib 활용예제 , 시각화
# 1. matplotlib 설치
#   visual studio code 터미널 창에 명령
'''
터미널 창에 명령
matplotlib 설치
> pip install matplotlib   # Windows
> pip3 install matplotlib  # Mac

matplotlib 삭제
> pip uninstall matplotlib # Windows
'''


import matplotlib.pyplot as plt     
'''
WARNING: You are using pip version 21.2.4; however, version 21.3.1 is available.
You should consider upgrading via the 'C:\Python310\python.exe -m pip install --upgrade pip' command.
'''
'''
# cmd 에서 'python -m pip install --upgrade pip' 명령어를 통해 업그레이드 해줄 수 있다.
'''

import matplotlib.pyplot as plt 
# x = [1,2,3,4]
# y = [1,3,5,7]
# plt.plot(x,y)
# plt.show()


x = list(range(1,13))
# x = range(12) # 0~11
# x = list(x)   # 0~11
# y = [1,3,5,7]
y = [3,3,6,10,14,18,23,24,20,15,9,5] # 제주 월별 최저기온

plt.xlabel('month')
plt.ylabel('degree')
plt.plot(x,y)
plt.show()

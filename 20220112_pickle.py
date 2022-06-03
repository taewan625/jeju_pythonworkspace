# pickle 파일, binary 2진 형태 파일 관리
# pickle은 2진 형태로 저장하고 가져오가 가지고 가고 하자는 것 -> 그래서 이렇게 공식을 써도 저장된 파일을 볼 때 외계어로 나옴
# 모드'wb', 'ab', 'rb'  # f 의  w, r, a 와 같은데 뒤에 b만 붙이면 됨

import pickle 
# pickle 파일 내용 저장
f = open('boxoffi.pickle','wb')
# pickle.dump('저장할 내용','저장장소파일 객체')
pickle.dump('123smple, 덤프 피클',f)
f.close()
# 메모장으로 열 때 다 깨져서 나옴
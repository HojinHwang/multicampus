# 모듈
# 함수, 클래스의 집합. 
# 별도의 파일로(*.py) 제작
# 함수<클래스<모듈<패키지
# 모듈의 종류
# 내부 모듈 - 기본적으로 제공
# 외부 모듈 - 설치후 사용 가능
# 사용자 정의 모듈 - 직접 제작해서 사용

# 모듈 import 문법
# import 모듈
# import 모듈 as 모듈별칭
# from 모듈 import 모듈함수 1,...

# 모듈안에 함수를 사용할때에는
# 모듈이름.함수(인자)

import math # math = 수학
import math as m # 별칭을 붙여줌으로써 math = m
from math import pi, sin
import random # random = 난수, 무작위수

print(math.pi) # 원주율
print(m.pi)
print(math.sin(10))
print(m.sin(10))

# 0 ~ 1 사이 소숫점으로 표시
# random.random()
# random.randrange(start,end,step)
print(random.random())
print(random.randrange(10))
print(random.randrange(0,51,2)) # 0~51사이의 2의배수 아무거나 하나
print(random.choice(['a','b','c','d'])) # 리스트의 아이템중 추출
# random.choice([리스트형태])
# random.shuffle(리스트 변수) - 리스트를 재배열
list_a = [1,2,3,4,5,6,7]
random.shuffle(list_a) # 이 과정을 거치고 프린트해야 나옴
# print(random.shuffle(list_a)) , None
print(list_a) # 랜덤으로 리스트를 재배열
import sys
print(sys.argv) # 현재 문서 경로가 표시
print(sys.version) # 컴퓨터 정보

import os
print(os.name)
# Curent Working Directory
print('현재 파일 폴더',os.getcwd()) # C:\pyclass = 현재 작업 폴더
print('모든 파일 목록',os.listdir()) # 현재 작업 폴더 안에 있는 모든 파일 목록








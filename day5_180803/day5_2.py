# 함수 < 클래스 < 모듈 < 패키지
# 함수안에는 실행문 + 변수 + 리스트 ...
# 클래스안에는 변수 개념을 속성으로 지정
#             함수 개념을 메소드로 지정
#             메소드의 집합
# 모듈은 파일간의 함수, 클래스 참조 가능
# 패키지는 모듈의 집합 


# 클래스 생성
# 클래스 선언
# class 클래스이름:
#   명령문

# square 클래스 선언 
# 가로와 세로 속성 
# def __init__(self,속성1):
#   self.속성1 = 속성

class square:
    def __init__(self,width,height):
        self.width = width
        self.height = height


# 클래스 타입
print(type(square)) # <class 'type'>

# 인스턴스 만들기
# 인스턴스에서 속성값 부여
# 인스턴스이름 = 클래스이름(속성값1,속성값2 ...)
s1 = square(50, 100)
s2 = square(100, 200)
print(type(s1)) # <class '__main__.square'>
print(' width = {}, height = {} '.format(s1.width,s1.height))

# car 클래스 만들기
class car:
    # 속성 만들기
    def __init__(self,brand,name,color,year):
        self.brand = brand
        self.name = name
        self.color = color
        self.year = year
        
# 인스턴스생성 및 속성값 부여
car1 = car('현대','스타렉스','회색','2010년')
car2 = car('기아','K5','흰색','2012년')
# 인스턴스이름.속성
print('car1 : {}, {}, {}, {} '.format(car1.brand,car1.name,car1.color,car1.year))
print('car2 : {}, {}, {}, {} '.format(car2.brand,car2.name,car2.color,car2.year))

# 퀴즈
# 주변에서 볼 수 있는 물체로 클래스를 선언하고
# 인스턴스화 시켜서 출력한다.

class bag:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color

bag1 = bag('아디다스','검은색')
bag2 = bag('나이키','흰색')
print('bag1 : {}, {} '.format(bag1.brand,bag1.color))
print('bag2 : {}, {} '.format(bag2.brand,bag2.color))
















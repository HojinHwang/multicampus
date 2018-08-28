# 자료형
# 정수 , 실수 , 문자열
# 리스트 , 튜플 , 딕셔너리 , 집합


# 리스트(list)
# 정의 리스트이름 = [아이템1,아이템2...]

fruits = ['사과','수박','망고','바나나']
print('fruits 목록 : {}'.format(fruits))
# 리스트 인덱싱
# 0부터 시작
# 음수일때는 역순 -1:마지막인덱싱값
print('fruits[0] = {}'.format(fruits[0])) # 사과
print('fruits[3] = {}'.format(fruits[3])) # 바나나
print('fruits[-1] = {}'.format(fruits[-1])) # 바나나

# 리스트 요소의 교체 
print('fruits 목록 : {}'.format(fruits))
fruits[0] = '자두'
print('fruits 목록 : {}'.format(fruits))

# 리스트 전체의 길이
# 
print('fruits 리스트 전체의 길이 : {}'.format(len(fruits)))

# 문자열 전체의 길이
# len(문자열변수나 문자열)
myStr = 'Python'
print('my Str 전체의 길이 : {}'.format(len(myStr)))

# 리스트의 슬라이싱 : 부분 추출
# 리스트이름[Start:End]
fruits = ['사과','수박','망고','바나나']
print(fruits[:]) # 전체출력
print(fruits[0:2]) # 0,1 인덱스 값 출력
print(fruits[2:]) # 2 부터 인덱스 값 출력
print(fruits)

# 리스트 추가
# 리스트이름.append(요소값)
# 마지막 위치에 추가
print('*'*30)
fruits = ['사과','수박','망고','바나나']
print(fruits)
fruits.append('복숭아')
print(fruits)

# 입력값을 리스트에 추가
drama = []
print('drama 리스트 : ',drama)
data = input('최근 본 드라마 제목을 입력하세요?')
drama.append(data)
print('drama 리스트 : ',drama)

# 리스트 추가 2
# 리스트이름.insert(위치인덱스,요소값)
# 인덱스에서 지정한 위치에 요소 삽입
numbers = [100,200,300,400]
print('numbers List = ',numbers)
# 첫번째 위치에 10 추가
numbers.insert(0,10)
print(numbers)
# 3번째 위치에 40추가
numbers.insert(2,40)
print(numbers)

# 리스트 삭제 1
# 리스트이름.remove(삭제할 요소값)
numbers = [100,200,300,400]
print('numbers List = ',numbers)
# 첫번째 요소 값 삭제
numbers.remove(100)
print('numbers List = ',numbers)

# 리스트 삭제 2
# 리스트이름.pop() - 마지막 위치의 요소 삭제한 후 값 리턴
# 리스트이름.pop(위치값) - 위치값에 해당하는 요소 삭제
fruits = ['사과','수박','망고','바나나']
print('fruits List = ', fruits )
fruits.pop()
print('fruits List = ', fruits)
fruits.pop(0)
print('fruits List = ', fruits)

# 리스트 삭제 3
# del 리스트이름[인덱스]
foods = ['라면','돈까스','볶음밥']
print('foods List = ',foods)
del foods[0]
print('foods List =',foods)

# 리스트값 역순으로 출력
# 리스트이름.pop()
# 마지막 위치의 요소 삭제한 후 값 리턴
foods = ['라면','돈까스','볶음밥']
print('foods List =',foods)
print(foods.pop())
#print('foods List = ', foods)
print(foods.pop())
#print('foods List = ', foods)
print(foods.pop())
#print('foods List = ', foods)


# 리스트 + 리스트 - 리스트 합하기
# 리스트이름 + 리스트이름
a = [1,2,3,4,5]
b = [7,8,9,10]
print(' a = ',a)
print(' b = ',b)
print(' a+b = ',a+b)
c = [1,2,3,4,5,6,7,8,9,10]
print(' c = ',c)
print(' a = ',a)
print(' b = ',b)

# 리스트이름*반복횟수 = 리스트 요소 반복하기
print('-'*30)
foods = ['라면','돈까스','볶음밥']
print(' foods = ',foods)
print(' foods*3 = ',foods*3)
print(' foods = ',foods)
foods2 = foods*3
print(' foods2 = ',foods2)

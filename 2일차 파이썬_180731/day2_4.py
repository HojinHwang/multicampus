# 자료 구조 변환 - 캐스팅
# 문자열 -> 리스트 1
# 문자열변수.split()
# 문자열의 공백을 기준으로 리스트 처리
# 문자열변수.split(구분자)
# 문자열의 구분자를 기준으로 리스트 처리

myStr = '안녕 무궁화 미나리'
print(myStr, type(myStr))
myList = myStr.split()
print(myList, type(myList))

myStr = '안녕/무궁화/미나리'
print(myStr, type(myStr))
myList = myStr.split('/')
print(myList, type(myList))

# 리스트 -> 문자열 2
# list(문자열)
# 문자열안에 등록되어 있는 
# #글자,공백 등 모두 분리되어 요소로 등록
myStr = '안녕 무궁화 미나리'
print(myStr, type(myStr))
myList = list(myStr)
print(myList, type(myList))

# str(리스트이름) -> ['아이템1',....]
myList = ['김','이','박']
print(str(myList))
result = str(myList)
print(result, type(result))
print(result[0]) 
print(result[1])

# 리스트 -> 문자열 2
# '구분자'.join(리스트)
myList = ['김','이','박']
print(myList, type(myList))
result = ' '.join(myList)
print(result, type(result))

# 리스트 요소 정렬하기
# 리스트이름.sort()
# 리스트이름.reverse()
# 조건 : 리스트 요소의 데이터형이 같아야 한다.
myNumbers = [1,100,67,50,40]
print(myNumbers)
myNumbers.sort() # 오름차순
print(myNumbers)
myNumbers.reverse() # 내림차순
print(myNumbers)
myList = ['Python','R','Java','C++']
print(myList)
myList.sort() # 알파벳 순서
print(myList)
myList.reverse() # 알파벳 역순
print(myList)

# 요소의 위치값(index) 반환
# 리스트이름.index(요소의값)
myNumbers = [1,100,67,50,40]
print('1은 {} 번째 저장되어 있습니다.'.format(myNumbers.index(1))) # index(값)

# 요소값이 몇개 들어가 있는가?
# 리스트이름.count(요소의값)
myNumbers = [1,100,67,100,100,50]
n = myNumbers.count(100)
print('100은 몇번 들어가 있나요 ?',n)
print(type(n)) # 정수






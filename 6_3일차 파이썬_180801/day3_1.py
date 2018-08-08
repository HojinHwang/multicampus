# 딕셔너리 정의 
# {키:값,... }
# 키값이 같을 경우에는 마지막에 정의한 것만 출력된다. 
dict1 = {'a':'africa','b':'banana','c':'cat'}
print('dict1 = ',dict1)
dict3 = {'africa':'a', 'banana':'b', 'cat' :'c'}
print('dict3 =', dict3)
dict2 = {'a':'africa','b':'banana','c':'cat','a':'abc'}
print('dict2 = ',dict2)

# 딕셔너리 요소 호출 
# 딕셔너리이름[키값]
print('dict1[\'a\'] = ',dict1['a'] )

# 딕셔너리 요소 추가 
# 딕셔너리이름[키값] = 값 
dict1 = {'a':'africa','b':'banana','c':'cat'}
print('dict1 = ',dict1)
dict1['d']='drive'
print('dict1 = ',dict1)

# 딕셔너리 요소 삭제 
# del 딕셔너리이름[키값]
dict1 = {'a':'africa','b':'banana','c':'cat'}
print('dict1 = ',dict1)
del dict1['a']
print('dict1 = ',dict1)

# 딕셔너리 함수 적용 

# 딕셔너리 요소 모두 삭제하기 
# 딕셔너리이름.clear()
dict2 = {'a':'africa','b':'banana','c':'cat'}
print('dict2 = ',dict2)
dict2.clear()
print('dict3 = ',dict2)

# 딕셔너리 요소중에서 키값만 모아서 재정의하기 
# 딕셔너리이름.keys() 
# 키값만 재정의해서 dict_keys 리스트로 저장 
dict3 = {'name':'홍길동', 'address':'서울 강남구','phone':'010-4567-9090'}
print('dict3 = ',dict3)
print(type(dict3))
# dict_keys(['name', 'address', 'phone'])
print(dict3.keys())
key_list = dict3.keys()
# <class 'dict_keys'>
print( ' 키리스트 = ', key_list, type(key_list) )

# 딕셔너리 요소중에서 값만 모아서 재정의하기 
# 딕셔너리이름.values()  
dict3 = {'name':'홍길동', 'address':'서울 강남구','phone':'010-4567-9090'}
print('dict3 = ',dict3)
# 값만 모아서 values_list에 저장 
values_list = dict3.values()
# <class 'dict_values'>
print( ' 값 리스트 = ', values_list, type(values_list) )

# 딕셔너리 요소에서 키,값 모아서 재정의하기 
# 딕셔너리이름.items() 
dict3 = {'name':'홍길동', 'address':'서울 강남구','phone':'010-4567-9090'}
print('dict3 = ',dict3)
# 키,값 모아서 items_list에 저장 
items_list = dict3.items()
# <class 'dict_items'>
print( ' 아이템 리스트 = ', items_list, type(items_list) )

# 딕셔너리 -> 문자열 
dict3 = {'name':'홍길동', 'address':'서울 강남구','phone':'010-4567-9090'}
print('dict3 = ',dict3)
print('문자열 변환 ', str(dict3))

# 키값만 모아서 문자열로 저장 
# '구분자'.join(딕셔너리이름)
myStr = ' '.join(dict3)
# name address phone
print(myStr)

# 딕셔너리 -> 리스트 
# 키값만 모아서 리스트로 저장 
# list(딕셔너리이름)
dict3 = {'name':'홍길동', 'address':'서울 강남구','phone':'010-4567-9090'}
print('dict3 = ',dict3)
dict_list = list(dict3)
print('dict_list = ', dict_list)

# 딕셔너리 -> 튜플 
# 키값만 모아서 튜플로 저장 
# tuple(딕셔너리이름)
dict3 = {'name':'홍길동', 'address':'서울 강남구','phone':'010-4567-9090'}
print('dict3 = ',dict3)
t_list = tuple(dict3)
print('t_list = ', t_list)

# 퀴즈 
'''
딕셔너리 구조로 차:브랜드 형태로 5개만 정의 
예) '레이':'기아'

딕셔너리 요소 추가 - 총6개 
딕셔너리 요소 삭제 - 총4개 
딕셔너리 마지막 요소의 값만 호출 
딕셔너리 구조에서 키값만 출력 
딕셔너리 구조에서 실제값만 출력 

'''

dict_car = {
    '레이':'기아',
    '소나타':'현대',
    '스타렉스':'현대',
    '말리부' : '쉐보레',
    'x1' : 'BMW'
    }
print(dict_car)
dict_car['라세티'] = '현대'   # 추가  
print(dict_car)
del dict_car['레이'] # 삭제
del dict_car['x1'] # 삭제
print(dict_car)
print(dict_car['라세티'])
print(dict_car.keys())
print(dict_car.values())





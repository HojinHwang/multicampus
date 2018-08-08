# 집합(set)
# 자료값의 중복을 허용하지 않는다. 
# {값1, 값2, ...}
# 순서가 없다 
# <class 'set'>

# 집합 정의 1 
# 집합이름 = set(리스트)


set1 = set([1,2,3,3,5,7])
# set1 =  {1, 2, 3, 5, 7}
print( 'set1 = ', set1)
# 집합 정의 2 
# 집합이름 = set(문자열)
set2 = set('banana')
print( 'set2 = ', set2)

# 집합 정의 3 
# 집합이름 = set(튜플)
set3 = set((1,2,3,4,5,66))
print( 'set3 = ', set3, type(set3) )

# 집합 연산 
# 합집합 
# 문법1 = 집합1|집합2
# 문법2 = 집합1.union(집합2)

set1 = set(['a','b','c','d','g'])
set2 = set(['a','b','c','d','f','e'])
print('set1 = ',set1)
print('set2 = ',set2)
print('set1 + set2 = ', set1|set2)
print('set1 + set2 = ', set1.union(set2))

# 교집합 : 두집합중 겹치는 아이템만 출력 
# 문법1 = 집합1 & 집합2
# 문법2 = 집합1.intersection(집합2)
print('set1 & set2 = ', set1&set2)
print('set1 & set2 = ', set1.intersection(set2))

# 차집합 : 첫번째집합에서 두번째집합 빼기 
# 문법1 = 집합1 - 집합2
# 문법2 = 집합1.difference(집합2)
print('set1 - set2 = ', set1-set2)
print('set1 - set2 = ', set1.difference(set2))

# 집합 요소 추가하기 1
# 집합이름.add(값)
set_name = set(['김씨','이씨','박씨','홍씨'])
print('set_name : ',set_name)
set_name.add('선우씨')
print('set_name : ',set_name)

# 집합 요소 추가하기 2
# 집합이름.update([값1,값2...])
# 여러개의 요소 추가시 사용 
set_name = set(['김씨','이씨','박씨','홍씨'])
print('set_name : ',set_name)
set_name.update(['신씨','정씨','선우씨'])
print('set_name : ',set_name)

# 집합 요소 삭제하기 
# 집합이름.remove(값)
set_name = set(['김씨','이씨','박씨','홍씨'])
print('set_name : ',set_name)
set_name.remove('홍씨')
print('set_name : ',set_name)

# 집합 -> 리스트 
set_name = set(['김씨','이씨','박씨','홍씨'])
print('set_name : ',set_name, type(set_name))
list_set_name = list(set_name)
print('list_set_name : ',list_set_name, type(list_set_name))

# 퀴즈 - 108, 109

a=1
b=1

print((a==b)or (a>b))
print(a == b)
print(a > b)
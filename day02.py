# 컬렉션 : List Tuple Dictionary Set
# 튜플 -> 고정(여러 데이터 타입) 변경x 인덱스로 접근, 중복o, 읽기만가능, 튜플이 리스트 보다 성능 좋음
# 리스트 -> 인덱스로 접근, 서로 다른 데이터 형을 함께 사용 가능
# 딕셔너리 -> 키:값, 순서x 인덱스x 키 값으로 접근, 테이블 구조
# 셋 -> 키x 인덱스x, 값만있음 주머니구조 무작위, 값들의 중복이 안됨
# immutable - 숫자형, 문자열, 튜플
# mutable - 리스트, 딕셔너리

#list
#indexing
a = []
print(type(a))
b = [1,2,3]
c = [1 ,2 ,'Life','is']
d = [1 ,2 ,['Life','is']]
print(d[2][0])

#slicing
a = [1,2,3,4,5]
print(a[0:3])

b = [5,6,7]
print(a+b)
print(b*3)
a.extend(b) #a 자체 늘이기
print(a)

b[2] = 4 # 수정하기
print(b)
b[1:2] = ['a','b','c']
print(b)

b[1:3] = []
print(b)
del b[1]
print(b)

a=['a','c','b']
a.reverse()
print(a)
a.sort()
print(a)
a.append('a')
print(a)
a.remove('a')
print(a)
print(a.pop())

a = ['Life','is','too','short']
result = ''.join(a)
print(result) #리스트를 문자열로 반환할 때 사용

fruits = ['사과','수박','망고','바나나','망고','바나나']
print('사과' in fruits)
print('fruits 목록 : {}'.format(fruits))
print('fruits[0] = {}'.format(fruits[0]))
print('fruits[-1] = {}'.format(fruits[-1]))
fruits[0] = '자두'
print('fruits 목록 : {}'.format(fruits))

x = 1
y = x
print(id(x), id(y), x, y)
#숫자는 immutable 이므로, 새로운 변수를 할당하므로 주소번지가 달라진다. 문자열도 마찬가지, 깊은 복사
y += 3
print(id(x), id(y), x, y)

x = [1, 2]
y = x
print(id(x), id(y), x, y)
# list 는 mutable이다, 얕은 복사
y.append(3)
print(id(x), id(y), x, y)

print('fruits 리스트 전체 길이 : {}'.format(len(fruits)))
fruits.append('복숭아')
print('fruits 목록 : {}'.format(fruits))
fruits.insert(1,'키위') #insert(번째,값)
print('fruits 목록 : {}'.format(fruits))

#삭제방법 : remove(값), del(index), slicing 빈 리스트 등등
fruits.remove('망고')
print('fruits 목록 : {}'.format(fruits))
print(fruits.pop())
print('fruits 목록 : {}'.format(fruits))
print(fruits.pop(0))
print('fruits 목록 : {}'.format(fruits))
del fruits[0:3]
print('fruits 목록 : {}'.format(fruits))
fruits.clear()
print('fruits 목록 : {}'.format(fruits))

a = [1,2,3,4,5]
b = [7,8,9,10]
print('a + b = ',a+b)
a.extend(b)
print(a)

foods = ['라면','돈가스','볶음밥']
print(' foods = ', foods)
sep = ','
print(sep.join(foods))

myStr = '강/김/홍/박/선우/우/이/신' #문자열 리스트로 나누기
print(myStr.split('/'))

#튜플 선언 ','가 중요하다.
tupleName = ('item',)
print(type(tupleName))
tupleName = 'item',
print(type(tupleName))
#튜플 삭제 변경시 오류 발생 함
#더하기 곱, 리스트와 같음

t1 = ('도','레','미','파','솔')
print(t1,type(t1))
t2 = 1,2,3,4,5
print(t2,type(t2))

myTuple = (100,'강아지',('지렁이'))
print('myTuple = ', myTuple)
print('myTuple[0] = ', myTuple[0])

myTuple += (50,100) #값 변경x 새로 만드는 것임
print('myTuple = ', myTuple)
myTuple += ('끝',)
print('myTuple = ', myTuple)

t1 = 100,50,30,30,30
print('30의 반복 횟수 : ',t1.count(30)) #sort 는 값이 수정되기 때문에 안됨
print(len(t1))
print(t1.index(30))

#튜플 형변환
myStr = 'Python'
print(myStr, type(myStr))
myTuple = tuple(myStr)
print(myTuple, type(myTuple))

myList = ['수학','과학','영어']
print(myList, type(myList))
myTuple = tuple(myList)
print(myTuple, type(myTuple))

myTuple = ('도','레','미')
print(myTuple, type(myTuple))
myStr = str(myTuple)
print(myStr, type(myStr))
print(myStr[0]) #(

myStr = ','.join(myTuple)
print(myStr,type(myStr))
myStr2 = ' / '.join(myTuple)
print(myStr2, type(myStr2))

#dictionary :키 값 중복x 나머지 값 중복가능, 순서x
#키 값이 같은 경우 마지막 아이템만 유지됨
#키 값으로 리스트 쓸 수 없다
dic1 = {1:'a',2:'b',3:'c'}
print(dic1,type(dic1))
dic1[4] = 'd'
print(dic1)
dic1[3] = 'e'
print(dic1)

del dic1[1] #del dic1[키]
print(dic1)

a = {'name' : 'pay', 'phone': '010555151151', 'birth' : '1994'}
print(a.get('name'))
print('name' in a) # 키 값으로만 찾기
print(a.pop('name'))
print(a)

dict1 = {'a':'africa', 'b':'banana', 'c':'cat'}
print('dict1 = ',dict1)
dict2 = {'a':'africa', 'b':'banana', 'c':'cat', 'a' : 'abc'}
print('dict2 = ',dict2, len(dict2))
dict0 = {}
dict0_0 = dict()
print('dict0 = ', dict0, type(dict0))

print(dict1.keys()) #키만, 값만, 둘다
print(dict1.values())
print(dict1.items())

myStr = ' '.join(dict1) #키 기준임
print(myStr)

#딕셔너리 얕은 복사
a = {'alice': [1, 2, 3], 'bob': 20, 'tody': 15, 'suzy': 30}
b = a.copy()
b['alice'].append(5)
print('a=', a)
print('b=', b)
#딕셔너리 깊은 복사
import copy
b = copy.deepcopy(a)
b['alice'].append(5)
print('a=', a)
print('b=', b) #구조체나 클래스 로 생각

t_list = tuple(a) #항상 키값 기준
print('t_list =', t_list)

a = {'alice': {1:'1', 2:'2', 3:'3'}, 'bob': 20, 'tody': 15, 'suzy': 30}
print(a['alice'][1]) #딕셔너리 안에 딕셔너리

# set 은 중복을 허용하지 않는다
# list를 set으로 형변환해서 합집합하는걸 많이 사용함
# 수정, 추가가능
s1 = set("hello")
print(s1) #중복제거

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print(s1 & s2, s1.intersection(s2)) #교집합
print(s1 | s2, s1.union(s2)) #합집합
print(s1 - s2, s2 - s1, s1.difference(s2), s2.difference(s1)) #차집합
s1.add(7)
print(s1)
s1.update([8,9,10]) #여러개 add하기
print(s1)
s1.remove(10) #없는거 빼면 에러 생김
print(s1) #빼기
s1.discard(9) #에러 없이 빼기
print(s1)
s1.clear() # 모든 컬렉션 자료형에 다있음
print(s1)


############################################################
# 로또 프로그램
import random

lotto = []
lotto.append(random.randint(1, 6)) # randint 난수는 원래 소수임, 따라서 난수를 정수로 주는
lotto.append(random.randint(1, 6)) # 함수이다 randint(1, 6) 이면 1~6까지범위 줌
lotto.append(random.randint(1, 6))
lotto.append(random.randint(1, 6))
lotto.append(random.randint(1, 6))
lotto.append(random.randint(1, 6))
print (len(lotto), lotto)

lotto = set() #set 초기화 방법
lotto.add(random.randint(1,6))
lotto.add(random.randint(1,6))
lotto.add(random.randint(1,6))
lotto.add(random.randint(1,6))
lotto.add(random.randint(1,6))
lotto.add(random.randint(1,6))
print (len(lotto), lotto)

lotto = set()
while True:
    lotto.add(random.randint(1, 6))
    if (len(lotto)) == 6:
        break

print(len(lotto), lotto)

k = range(1,47) #(상한값, 하한값, 인터벌)
lott_num = random.sample(k,6)
print(lott_num)

f = random.random()
print(f)

f = random.uniform(1.0, 36.5)
print(f)

i = random.randrange(1, 101, 2) # 1~100 사이의 짝수
print(i)

i = random.randrange(10) # 끝값 = (0,10,1)
print(i)
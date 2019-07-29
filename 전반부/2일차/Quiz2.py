# 1. a, b, c, d, e를 저장하는 튜플을 만들고 첫 번째 튜플값과 마지막 번째 튜플값을 출력하세요.
myTuple = ('a','b','c','d','e')
print(myTuple[0],myTuple[-1])

# 2. 다음 코드를 작성해서 실행해보고 에러가 나는 이유를 설명하세요.
# tupledata = ('dave', 'fun-coding', 'endless')
# tupledata[0] = 'david'
#튜플은 immutable 이기 때문에 수정할 수 없다.

# 3. 다음 튜플 데이터를 리스트 데이터로 변환한 후에 'fun-coding4' 데이터를 마지막에 추가하고,
#    다시 튜플 데이터로 변환하세요.
tupledata = ('fun-coding1', 'fun-coding2', 'fun-coding3')
temp = list(tupledata)
temp.append('fun-coding4')
tupledata = tuple(temp)
print(tupledata)

# 4. 비어 있는 튜플, 리스트, 딕셔너리 변수를 하나씩 각각 만드세요.
mt = ()
ml = []
md = {}

# 5. 다음 actor_info 딕셔너리 변수를 만들고, 홈페이지, 배우 이름, 최근 출연 영화 갯수를 다음과 같이 출력하세요

actor_info = {'actor_details': {'생년월일': '1971-03-01',
                   '성별': '남',
                   '직업': '배우',
                   '홈페이지': 'https://www.instagram.com/madongseok'},
 'actor_name': '마동석',
 'actor_rate': 59361,
 'date': '2017-10',
 'movie_list': ['범죄도시', '부라더', '부산행']}


#배우 이름: 마동석
#홈페이지: https://www.instagram.com/madongseok
#출연 영화 갯수: 3
print('배우이름 : ',actor_info.get('actor_name'))
print('홈페이지 : ',actor_info.get('actor_details').get('홈페이지'))
print('출연 영화 갯수 : ',len(actor_info.get('movie_list')))

# 6. 다음 리스트에서 "Apple" 항목만 삭제하세요. : ["Banana", "Apple", "Orange"]
mlist = ["Banana", "Apple", "Orange"]
mlist.remove('Apple')
print(mlist)

# 7. 다음 튜플을 리스트로 변환하세요. : (1,2,3,4)
mtuple = (1,2,3,4)
mlist = list(mtuple)
print(mlist)

# 8. 다음 항목을 딕셔너리(dict)으로 선언해보세요. : <성인 - 100000 , 청소년 - 70000 , 아동 - 30000>
mdict = {}
mdict['성인'] = 100000
mdict['청소년'] = 70000
mdict['아동'] = 30000
print(mdict,type(mdict))

# 9. 8번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.
mdict['소아'] = '0'
print(mdict,type(mdict))

# 10. 8번에서 선언한 딕셔너리(dict)에서 Key 항목만 출력해보세요.
print(list(mdict.keys()))

# 11. 8번에서 선언한 딕셔너리(dict)에서 value 항목만 출력해보세요.
print(list(mdict.values()))

#연습문제####
#3,4
pin = '881120-1068234'
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd,num,pin[7])

#5
a='a:b:c:d'
print(a.replace(':','#'))

#6
a=[1,3,5,4,2]
a.sort()
print(a)
a.reverse()
print(a)

#7
a = ['Life', 'is', 'too', 'short']
result = ' '.join(a)
print(result)

#8
a = (1, 2, 3)
a =  a + (4,)
print(a)

#9
a = dict()
#a[[1]] = 'python'
print(a)

#10
a = {'A':90, 'B':80, 'C': 70}
result = a.pop('B')
print(a,'\n', result)

#11
a = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a)
b = list(aSet)
print(b)

#12
a = b = [1, 2, 3]
a[1] = 4
print(b)
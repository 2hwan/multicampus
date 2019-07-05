# 조건문 반복문
# 논리 연산자 and, or, not
# if, if else, if elif else
# : 로부터 같은 레벨은 같은 들여쓰기
# IndentationError : 들여쓰기 에러 , shift + tab 땡겨오기
# if ~ in [], if ~ not in []
# :뒤에 아무것도 없으면안됨, pass 사용 이유, 수도코드
# !가 아니라 not, ! 써도 되는데..?

a = 1
b = 10
if a > b :
    print('a는 b보다 크다')
else :
    print('a는 b보다 작다')

money  =  1
if money : print('택시를 타고')
print('가자')

#data = int(input('정수를 입력 하세요'))
data = 1
if data > 0 : print('양수')
elif data <0 : print('음수')
else : print('0')

# age = int(input('나이 입력 : '))
age = 26
if age > 19 : print('성인')
elif 17 <= age : print('고등학생')
elif 14 <= age : print('중학생')
elif 8 <= age  : print('초등학생')
else : print('유아')

num = 2
if num % 2 : print('홀')
else : print ('짝')

# k = int(input('키를 입력하세요 : '))
# w = int(input('무게를 입력하세요 : '))
k = 170
w = 60
bmi = (w/((k/100)**2))
print('bmi = %.2f'% bmi)
if 35 < bmi : print('고도비만')
elif 30 <= bmi : print('중고도비만')
elif 25 <= bmi : print('경도비만')
elif 23 <= bmi : print('과체중')
elif 18.5 <= bmi : print('정상')
else : print('저체중')

animal = ['원', '닭', '개','돼지','쥐', '소', '범', '토', '용', '뱀', '말', '양']
#year = int(input('몇년생?'))
year = 1994
print ('당신은 {0}년도에 태어난 {1} 띠 이시군요'. format(year,  animal[year % 12]))

#문자열에서 in과 not in을 사용 할 수 있다

e = {'name' : 'kim', 'city': 'seoul', 'grade' : 'b'} #딕셔너리는 암말없으면 키로 비교
print('name' in e)
print('seoul' in e.values())

#score = float(input('')) #float 형변환
score = 4.5
if score == 4.5 : print('신')

# 시간은 문자열과 datetime이 다르다
# format 이 중요하다
import datetime
now = datetime.datetime.now()

print(' now = ',now)
print(' 년도 = ',now.year)
print(' 월 = ',now.month)
print(' 일 = ',now.day)
print(' 일 = ',now.date())
print(' 시 = ',now.hour)

print(' 오늘은 {} 년 {} 월 {} 일 입니다.'. format(now.year, now.month, now.day))

print(' 작성일자 {}'.format(now.strftime('%Y-%m-%d %H:%M:%S'))) #Y년 m월 d일, H시간 M분 S초

newdt = datetime.datetime.strptime('1994-07-15', '%Y-%m-%d')
print(newdt, now, type(newdt) , type(now))

print(now-newdt) #datetime 끼리 계산 가능

newd = datetime.timedelta(days=100) #miniutes, hours, weeks, years
print(now+newd)

# while, continue, break, ~비트 연산
i = 0
while i < 10 :
    i += 1
    if not i%2 : continue
    print(i)

sum = 0
i = 0
while i < 100 :
    i += 1
    if i % 5 > 0 : continue
    sum += i
print(sum)

# for 변수 in (iterator 개체) :
sum = 0

for nemo in range(1,101) :
    if not nemo % 5 :
        sum += nemo
print(sum)

aa = [('a', 'b'), ('c', 'd'), ('e', 'f')]
for (i, j) in aa:
    print(i+j)

for i in range(0,21,2):
    if not i : pass

for i in range(2,10) :
    for j in range(1,10) :
        print('%d x %d = %2d'% (i ,j , i*j) ,end='\t')
    print('')

for i in range(2,10) :
    for j in range(1,10) :
        print('{0}*{1}={2:2}'.format(i, j, i*j) ,end='\t')
    print('')
print('')
for j in range(1,10) :
    for i in range(2,10) :
        print('%d x %d = %2d'% (i ,j , i*j) ,end='\t')
    print('')
print('')


for k in range(1,4) :
    for j in range(1,10) :
        for i in range(3*k-1,3*k+2) :
            print('%d x %d = %2d'% (i ,j , i*j) ,end='\t')
        print('')
    print('')

# for 문과 list 내포
myl = []
for num in range(1,6) :
    myl.append(num*3)
print(myl)

mylist = [num*3 for num in range(1,6)]
print(mylist)

print([x*y for x in range(2,10) for y in range(1,10)]) #이중 for문 list 내포

gugu = [i*5 for i in range(1,100) if i%2 == 0] #for문 if 문 list 내포
print(gugu)

for i in range(1,6):
    print('*'*i)

i = 0
while i < 5 :
    i += 1
    print('*' * i)

i = 0
sum = 0
while i < 50 :
    i += 1
    sum += i
print(sum)
#
# while 1 :
#     ans = input('아무거나 입력, 종료시 x')
#     if ans == 'x' or 'X':
#         print('종료')
#         break
#
# while 1 :
#     ans = input('아무거나 입력, x 종료시 ')
#     if ans == 'x'.upper():
#         print('종료')
#         break

#iterator 개체: range, reversed, enumerate, filter, map, zip

cnt = 1
for i in ['a','b','c'] :
    print('요소 {} : {}'.format(cnt,i))
    cnt += 1

myList = [50, 44, 100, 30, 1, 300, 500]
myList.sort()
myList.reverse()
print(myList[0])

myList = [50, 44, 100, 30, 1, 300, 500]
result = myList[0]
for i in myList:
    if result < i:
        result = i
print(i)

my_info = {'name' : 'Kim','age':33,'city':'Seoul'}
for key in my_info:
    print(key, ':', my_info[key]) #키와 value

for key, val in my_info.items() :
    print(key,':',val)

#for의 else
numbers = [14, 2, 33, 15, 38]

for num in numbers:
    if num == 39:
        print('found : 33!')
        break
    else:
        print('not found : ', num)
else:
    print('not found 39...') #for문이 break없이 정상 실행 됬을 때 이동


for num in numbers:
    if num == 33:
        print('found : 33!')
        break
    else:
        print('not found : ', num)
else:
    print('not found 39...') #for문이 break없이 정상 실행 됬을 때 이동
numbers =[]
for num in numbers:
    if num == 33:
        print('found : 33!')
        break
    else:
        print('not found : ', num)
else:
    print('not found 39...') #for문이 break없이 정상 실행 됬을 때 이동









a = 1.5















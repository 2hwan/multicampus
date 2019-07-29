
print('hello', end=', ')
print('hello', end=', ')
print('hello', sep='\n')
# shift alt e
# ctrl /

print('hello', 'hello','hello', sep='')

# \b 백스페이스 \r 맨 앞쪽으로 커서 보내기

print('I\'m XXX') # \' '출력
print("I'm XXX")
print("I'm \"XXX\"") #쌍이 맞아야 함

#아스키값 받나?

a = b = 1
print(type(a), id(a), id(b), a is b) #type 자료형, id 참조값
print(a is b) #레퍼런스 값이 같니?
print(a == b) #값이 같니?
print(a)
print(b)
b=2
print(id(a), id(b))
print(a,b)
print(a is b)
print(a == b)

a, b = b, a #swap 이 이렇게 된다
print("a: ", a,"b: ",b)

import this
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))

a = None
#del(a) #변수 삭제
print(a,b)

a = 'A'
print('%d %c', a, a) #?????????

#a = input("What is your name? ") #다 문자열임
print(a)

print(ord(a)) #아스키 문자 -> 숫자
print(chr(ord(a))) #아스키 숫자 -> 문자
import sys
print(sys.maxsize) #2147483647
print(sys.maxsize +1) #2147483648

num = 231412341234124132412341234
print(num, type(num))

num2 = 2*5*3.14
print(num2,type(num2)) #31.400000000000002 0.000000000000002 기본소수 15자리 표현, 부동소숫점 오차
#복소수 j

print(sys.stdout.encoding)
print(sys.stdin.encoding) #인코딩 : UTF-8

print(
"""
asdfasdfas
asdfasdfasdf
asdfasdfsadf
""")
"""여러줄 주석
    도됨
    쿼리 문 작성할 때 좋다"""

a = (100 == 100)
b = (10 > 100)
print(a,b)

#a = input("number")
#b = input("number2")

print(a+b)
print(int(a)+int(b))

a = 2**3 #2의 3승
a = 7//4 #나눗셈의 몫

# && -> and || -> or

print("Python" + "3.7")
print("Python", 3.7)

print("*" * 50)

a = 'Life is too short, You need Python'
print(a[0], a[12], a[-1]) #index
print(a[0:4], a[5:7]) #slicing 0부터 3까지 5부터 6까지

a = '20190703Rainy'
date = a[:8]
print(date, a[8:] , a[8:len(a)-1])
print(a[0:12:3]) #interval 건너뛰기

addr1 = '서울시'
addr2 = '서초구'
addr3 = '역삼동'
addr4 = '멀티로 123'
print(addr1, addr2, addr3, addr4)
print(addr1 +' '+ addr2 +' '+ addr3 +' '+ addr4)
print("우리집 주소는 {0} {1} {2} {3}". format(addr1, addr2, addr3, addr4)) #format 튜플타입
print("우리집 주소는 {} {} {} {}". format(addr1, addr2, addr3, addr4))
print("우리집 주소는 {0} {1} {2} {0}". format(addr1, addr2, addr3)) #번호를 주는게 좋음
print("%s %s" % (addr1, addr2))
print("%10s %s" % (addr1, addr2))
print("{0:d} {1:5d} {2:05d}". format(123, 123, 123)) #데이터 분석할 때 씀
print('value1: {a}, value2: {b}'. format(a = 'dog',b = 20)) #콕콕 찝어주기

a = 'A'
print("%d %c" % (ord(a),a))

a = 'hobby'
print(a.count('b')) #갯수 찾기, 있는지 없는지 찾을 때 씀

a = "  Python is best choice"
print(a.find('b'), a.find('k')) #위치 값 반환, 없으면 -1
print(a.index('t'))
#print(a.index('k')) #인덱스는 없으면 오류가 남

b = '@'
print(b.join('abcd'))
print(b.join('abcd').split('@'))
print(a.split())

print(a.upper(), a.upper().lower(), a.strip(), a.replace(" ",""), a.replace("best","worst"), sep='\n') #대소문자, 공백 없애기, 바꾸기

a = "Pithon"
print(a)
#a[1] = 'y' # 이거 안됨
a = a[:1] + 'y' + a[2:]
print(a)

stName3 = stName4 = '기생충'
print(stName3 == stName4)
print(stName3 is stName4)

a = b = 10
print(a is b)

c = 10
print(a is c)

beer = input()
if(beer is 'cass'):
    print ('cass is favorite beer!') #실행안됨
if(beer == 'cass'):
    print ('cass is favorite beer!') #실행됨

num = int(input())
if(num is 7):
    print ('My favorite number is 7')

hong = '881120-1068234'
print(hong[:6],hong[-7:])
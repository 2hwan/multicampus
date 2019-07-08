# 함수 < 클래스 < 모듈 < 패키지
# def 함수명(입력 인수) :
#    <수행할 문장 1>
#    <수행할 문장 2>
# 여러개 한꺼번에 return이 가능하다

def sum_mul(n1, n2):
    return n1 + n2, n1 * n2


print(sum_mul(3, 5))
result = sum_mul(3, 5)  # 튜플로 받기
x, y = sum_mul(3, 5)  # 각각 받기
print(type(result))
print(' 합은 {}, 곱은 {} 입니다.'.format(result[0], result[1]))


def say_myself(name, old, man=True):  # 미리 기본 값 주기, 기본 값을 주면 안넘겨줘도 된다
    print('나의 이름은 %s 입니다.' % name)  # 기본 값은 뒤로
    print('나이는 %d살 입니다' % old)
    if man:
        print('남자입니다')
    else:
        print('여자 입니다')


say_myself('홍길동', 17)
say_myself('기본값', 17, False)


def say_myself(name, man=True, old=10):  # 미리 기본 값 주기, 기본 값을 주면 안넘겨줘도 된다
    print('나의 이름은 %s 입니다.' % name)  # 기본 값은 뒤로
    print('나이는 %d살 입니다' % old)
    if man:
        print('남자입니다')
    else:
        print('여자 입니다')


say_myself('홍길동', old=20)  # 파라미터가 여러개인경우 이름까지 넘겨줘야함
say_myself('홍길동', man=False, old=20)


# 가변 인자 함수
# 가변 입력 값 : *args : tuple, **kwargs : dictionary

def add(a, b, c):  # 파이썬은 함수 이름이 달라야한다.
    print(a + b + c)  # 오버로딩 안됨(중복정의), 오버 라이딩 됨(재정의)


add(2, 3, 4)


def add_arg(*args):
    total = 0
    for arg in args:
        total += arg
    print(total)


add_arg(1, 2, 3, 4, 5)


def cal(choice, *args):  # 가변아닌게 앞으로
    if choice == 'Sum':
        result = 0
        for i in args:
            result += i
    elif choice == 'Diff':
        result = 0
        for i in args:
            result -= i
    print(result)


cal('Diff', 1, 2, 3)


def myNum(**kwargs):
    print(kwargs)
    print('First value : {first}'.format(**kwargs))
    print('Second value : {second}'.format(**kwargs))


myNum(first=1, second=2)


def kwargs_func(**kwargs):
    for v in kwargs.keys():
        print('{} {}'.format(v, kwargs[v]), end=' ')
    print()


kwargs_func(name1='Kim')
kwargs_func(name1='Kim', name2='Park')
kwargs_func(name1='Kim', name2='Park', name3='Lee')


def kwargs_funci(**kwargs):
    for k, v in kwargs.items():
        print('{} {}'.format(k, v), end=' ')
    print('ck')


kwargs_funci(name1='Kim')
kwargs_funci(name1='Kim', name2='Park')
kwargs_funci(name1='Kim', name2='Park', name3='Lee')


def args_func(*args):
    for i, v in enumerate(args):  # enumerate 알아서 스스로 인덱스를 붙여줌
        print('{}'.format(i), v, end=' ')
    print()


args_func('Kim')
args_func('Kim', 'Park')
args_func('Kim', 'Park', 'Lee')


def example(arg_1, arg_2, *args, **kwargs):  # 섞었을 때 우선순위: 고정, 가변, 기본값
    print(arg_1, arg_2, args, kwargs)


example(10, 20)
example(10, 20, 'park', 'kim')
example(10, 20, 'park', age1=33, age2=34)
example(10, 20, 'park', 'kim', 'lee', age1=33, age2=34, age3=44)


def bmi(a, b):
    result = (b / ((a / 100) ** 2))
    print('bmi = %.2f' % result)
    if 35 < result:
        print('고도비만')
    elif 30 <= result:
        print('중고도비만')
    elif 25 <= result:
        print('경도비만')
    elif 23 <= result:
        print('과체중')
    elif 18.5 <= result:
        print('정상')
    else:
        print('저체중')


bmi(170, 60)

# * 리스트나 튜플 언팩킹
# ** 딕셔너리 키, 값 언팩킹

lst = [11, 3, 4, 5, 'list']
print(lst)
print(*lst)

kwargs = {'first_name': 'john', 'last_name': 'doe', 'username': 'johndoe', 'email': 'jhlee@asdf', 'passwrd': '1234'}

print(*kwargs)  # 키들만 언팩킹
print('첫번 째 key : {0}, 두번째 key : {1}'.format(*kwargs))

# 딕셔너리의 키: 값으로만 언팩킹
print('first_name : {first_name}, last_name : {last_name}'.format(**kwargs))


# 전역변수가 Rvalue면 b = a+2 전역변수 값을 읽어온다
# Lvalue 쪽으로 오면  지역
# global a 로하면 전역씀

def call_by_value(num, mlist):
    num = num + 1
    mlist.append('add 1')


num = 10
mlist = [1, 2, 3]

print(num, mlist)
call_by_value(num, mlist)
print(num, mlist)


# 중첩함수 내포함수

def nested_func(num):
    def func_in_func(num):
        print(num)

    print('in func')
    func_in_func(num + 100)


nested_func(1)


def gugu(p):
    for j in range(1, 10):
        print('%d x %d = %2d' % (p, j, p * j), end='\t')


gugu(6)
print()

# 람다 함수
# 익명 함수
# 쓰고 버리는 일시적인 함수
# 메모리 절약 가능하다

f = lambda x, y: x + y
print(f(4, 4))

f = lambda x: x ** 2
print(f(8))

print((lambda x, y: x + y)(12, 20))

f = lambda x: x * 10
t = lambda x, y: x * y

print(f(2))
print(f(5))
print(t(2, 6))


# 고차함수
def func_final(x, y, func):
    result = x * y * func
    return result


print(func_final(10, 10, f(10)))


def circle_area(radius, print_format):
    area = 3.14 * (radius ** 2)
    print_format(area)


def precise_low(value):
    print('결과값: ', round(value, 1))


def precise_high(value):
    print('결과값: ', round(value, 2))


circle_area(3, precise_low)
circle_area(3, precise_high)

# 함수의 스코프
x = 'global'


def outer():
    x = 'local'  # 내부 x 로컬로 생성

    def inner():
        nonlocal x  # x는 로컬이아니다 --> local
        x = 'nonlocal'  # x값 nonlocal로 local 값이 바뀜
        print('inner:', x)  # non local

    inner()
    print('outer:', x)


outer()
print('global :', x)


def scope_test():
    def do_local():
        spam = 'local spam'
        print('dolocal', spam)

    def do_nonlocal():
        nonlocal spam
        spam = 'nonlocal spam'

    def do_global():
        global spam
        spam = 'global spam'

    spam = 'test spam'
    do_local()
    print('After local assignment:', spam)
    do_nonlocal()
    print('After nonlocal assignment:', spam)
    do_global()
    print('After global assignment', spam)


scope_test()

# 람다함수 시리즈 3개 map, filter, reduce
arr = [1, 2, 3, 4, 5]
brr = map(lambda x: x ** 2, arr)
print(brr)
crr = list(brr)
print(crr)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
brr = filter(lambda x: x % 3 == 0, arr)  # 조건이 맞는지 필터링
print(brr)
for item in brr:
    print(item, end=' ')


def oneto100():
    sum = 0
    for i in range(1, 101):
        sum += i
    return sum


print(oneto100())

# import numpy as np
# print(np.sum([x for x in range(1,101)]))

print(divmod(7, 3))  # 몫 과 나머지

print(eval('1+2'))  # 문자열 수식처리
print(eval("'hi'+'a'"))
print(eval('divmod(4, 3)'))

my_list = ['apple', 'banana']
for index, value in enumerate(my_list, 1):  # 색인부여 (,시작번호)
    print(index, value)

actor = ['정우성', '나나']  # zip
gender = ['여', '여']
for i, j in zip(actor, gender):
    print(i, '-', j)

actor = [('나나', '정우성'), ('여', '남')]
a, b = zip(*actor)
print(a, b)

print('-10 :', abs(-10))

result = divmod(10, 5)
print(result, type(result))

import math

print(math.ceil(5.1)) #올림
print(math.ceil(8.999))

print(math.floor(3.874)) #내림
print(math.floor(-25.5))

print(math.pi)

data = '5*9'
print(data)
result = eval(data)
print(data, '=', result)

print('최대값', max([34,50,100,1,20]))
print('최소값', min([34,50,100,1,20]))

aList = [78,90,80,50]
bList = [8,100,34,60]

newl = aList + bList
print('최대값', max(newl))
print('최소값', min(newl))

my_list = ['바나나','사과','수박','포도']
for i,v in enumerate(my_list,1) :
    print(v,i)

result = list(enumerate(my_list,1))
print(result)
print(result[0])

str1 = '가나다'
str2 = '1234'
print(str1.isalpha())
print(str1.isdigit())
print(str2.isalpha())
print(str2.isdigit())

result_list = []
while 1 :
    if len(result_list) == 5 :
        print(result_list)
        break
    else :
        data = input('입력')
        if data.isdigit() :
            result_list.append(data)
        else :
            print('숫자만 입력하세요')


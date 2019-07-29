# 모듈 import, form 모듈 import 클래스
# 표준 모듈. 외부 모듈, 사용자 정의 모듈

class FourCalc :

    def __init__(self, num1 = None, num2 = None):
        self.first = num1
        self.second = num2

    def add(self) :
        return self.first + self.second

    def sub(self) :
        return self.first - self.second

    def mul(self) :
        return self.first * self.second

    def div(self) :
        return self.first / self.second

class MoreFourCalc(FourCalc) :
    add_num = 10

    @classmethod
    def setPI(cls):
        pass

    @staticmethod
    def setPI():
        pass

    def pow(self):
        return self.first**self.second

    def div(self) :
        if self.second == 0:
            return 0
        else : return self.first / self.second

# 사용자 정의 모듈
# 테스트 해보기
if __name__ == "__main__" : #이 자체를 실행한 경우만 들어감, 다른데서 import할 때는 실행 안 됨
    a = FourCalc(5, 7)
    print(a.add(), a.sub(), a.mul(), a.div())

    b = FourCalc(10, 5)
    print(b.add(), b.sub(), b.mul(), b.div())

    # c = FourCalc(5, 0)
    # print(c.div())
    #
    ch_a = MoreFourCalc(10, 2)
    print(ch_a.add(), ch_a.sub(), ch_a.mul())
    print(ch_a.div(), ch_a.pow())

    ch_b = MoreFourCalc(8, 2)
    print(MoreFourCalc.add_num,id(MoreFourCalc.add_num))
    print(ch_a.add_num,id(ch_a.add_num))
    print(ch_b.add_num, id(ch_b.add_num))

    #MoreFourCalc.add_num = 20
    ch_a.add_num = 20 # 객체 명으로 클래스 접근 x
    print(MoreFourCalc.add_num,id(MoreFourCalc.add_num))
    print(ch_a.add_num,id(ch_a.add_num))
    print(ch_b.add_num, id(ch_b.add_num))

import sys
# 현재 문서 경로가 표시
print(sys.argv)
print(sys.path) #list 로 줌, sys.path.append() 로 찾을 수 있음

#sys.exit()
print(sys.version)
print(sys.version_info)
print(dir(sys))


import math
# 수학 함수
print(math.pi)

# 프로그램 시작할 때 넘기고 싶을 때 사용
print('명령줄 인수 체크하기!!') # 터미널에서 넘기기 /python day06.py 12 34 abc 가나다 or run -> configuration
for n in sys.argv:
    print(n)

#print('\n\n파이썬의 sys.path 디렉토리', sys.path)

import os
print(os.name)
# 디렉토리 정보
print(os.getcwd())
print(os.listdir())

if not os.path.isdir('test'):
    os.mkdir('test')
elif os.path.exists('test'):
    os.rmdir('test')

from urllib import request

target = request.urlopen('http://google.com')
output = target.read()
print(output)

from datetime import datetime
now = datetime.now()
print(now.year, '년')
print(now.month, '월')
print(now.day, '일')

import glob

print(glob.glob('*.*'))
print(glob.glob('C:\Temp\*.txt'))

import webbrowser
# webbrowser.open('http://google.co.kr')

foodList = [('갈비만두',4000), ('김치만두', 3000), ('물만두', 2000)]

for i in zip(*foodList): # 쪼갬
    print(i)
# pyc 파일 : 컴파일된 파이썬 바이너리 파일
# 모듈을 호출할 때 빠르게 호출 하기 위해

#-----------------------------------------------------------------#
# 패키지 pakage : 모듈의 묶음
# 라이브러리리

# 에러처리, 예외처리

class InputValueError(Exception): # 만들어도 되고 안만들어도 되고
    def __init__(self, msg='입력값 오류입니다'):
        self.msg = msg

    def __str__(self):
        return self.msg

from random import randint

n = randint(1,100)
print(n)

while 1 :

    ans = input('num : ?, Q (to exit)' )

    if ans.upper() == 'Q':
        break
    try:
        if not 0 < int(ans) < 101:
            raise Exception('1~100 사이의 숫자를 입력하세요') #그냥 간단하게 이렇게 해도됨
            # raise InputValueError('1~100 사이의 숫자를 입력하세요')
        ians = int(ans)
        if n == ians :
            print('correct')
            break
        elif n > ians : print('up')
        else : print('down')

    except ValueError :
        print('숫자입력!!')
    except Exception as err :
        print(err)




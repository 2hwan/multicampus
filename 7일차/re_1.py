# 정규표현식 - 입력값이 정확한지 처리
# 모듈 re 
import re

str = 'My id number is kim0902'

# findall(정규표현식패턴,문자열)
a = re.findall('a',str)
print(a)  # []
b = re.findall('kim',str)
print(b)  # ['kim']
c = re.findall('m',str)
print(c)  # ['m', 'm']
print('-'*30)

# 복잡한 패턴 예제
# 정규표현 패턴 [a-z], [A-Z], [0-9]
# 정규표현 패턴 [a-z]+, [A-Z]+, [0-9]+ - 단어단위로 찾음 
str = 'My id number is kim0902'

# 소문자를 모두 찾아서 리스트로 반환
s1 = re.findall('[a-z]',str)
print(s1)
# ['y', 'i', 'd', 'n', 'u', 'm', 'b', 'e', 'r', 'i', 's', 'k', 'i', 'm']

# + 반복옵션, 소문자를 하나씩 끊어서 찾지 않고 연속해서 찾음. 
# 단어 단위리스트로 반환
s2 = re.findall('[a-z]+',str)
print(s2)
# ['y', 'id', 'number', 'is', 'kim']

# 대문자를 모두 찾아서 리스트로 반환
s3 = re.findall('[A-Z]',str)
print(s3)
# ['M']

# 숫자를 모두 찾아서 리스트로 반환
s4 = re.findall('[0-9]',str)
print(s4)
# ['0', '9', '0', '2']

#  + 반복옵션, 숫자를 하나씩 끊어서 찾지 않고 연속해서 찾음. 
# 단어 단위리스트로 반환
s5 = re.findall('[0-9]+',str)
print(s5)
# ['0902']
print('-'*30)


# 정규표현 패턴 알아보기 
str = 'My id number is 김_kim_0502$'

# 소문자,대문자, 숫자(문자 단위)
a = re.findall('[a-zA-Z0-9]',str)
print(a)
# ['M', 'y', 'i', 'd', 'n', 'u', 'm', 'b', 'e', 'r', 'i', 's', 'k', 'i', 'm', '0', '5', '0', '2']

# 소문자,대문자, 숫자(단어단위)
b = re.findall('[a-zA-Z0-9]+',str)
print(b)
# ['My', 'id', 'number', 'is', 'kim', '0502']

# ^(not),소문자,대문자, 숫자가 아닌 문자들(공백문자, 특수문자)
c = re.findall('[^a-zA-Z0-9]+',str)
print(c)
# [' ', ' ', ' ', ' ', '_', '$']

# 영문자, 숫자, _
d = re.findall('[\w]',str)
print(d)
# ['M', 'y', 'i', 'd', 'n', 'u', 'm', 'b', 'e', 'r', 'i', 's', 'k', 'i', 'm', '_', '0', '5', '0', '2']

# 영문자, 숫자, _, 단어단위
e = re.findall('[\w]+',str)
print(e)
# ['My', 'id', 'number', 'is', 'kim_0502']

# 영문자, 숫자, _ 가 아닌경우
f = re.findall('[\W]',str)
print(f)
# [' ', ' ', ' ', ' ', '$']
print('-'*30)



# 비밀번호 정합성 체크 함수
def pwd_check(pwd):
    # 비밀번호 길이 확인 (6~12)
    if len(pwd) < 6 or len(pwd) > 12:
        print('비밀번호의 길이가 적당하지 않습니다.')
        return False
    # 숫자 혹은 알파베스 유무 확인 
    # 특수문자 걸러짐. 영문자, 숫자만
    # findall() 리스트로 리턴. [0] 첫번째 요소밖에 없다.
    if re.findall('[a-zA-Z0-9]+',pwd)[0] != pwd:
        print(pwd, '==> 숫자와 영문자로만 구성되어야 합니다.')
        return False
    # 알파벳 대문자 확인 
    # 소문자의 길이가 0이거나 대문자의 길이가 0이면
    if len(re.findall('[a-z]',pwd))==0 or len(re.findall('[A-Z]',pwd)) ==0:
        print('대문자와 소문자 모두 필요합니다.')
        return False
    print(pwd, '올바른 비밀번호입니다.')

pwd_check('12abc')          # 비밀번호의 길이가 적당하지 않습니다.
pwd_check('123abc')         # 대문자와 소문자 모두 필요합니다.
pwd_check('123Abc*')        # 숫자와 영문자로만 구성되어야 합니다.
pwd_check('xcv467rtA')      # xcv467rtA 올바른 비밀번호입니다.

print('-'*30)


# Email 주소 체크
def email_check(email):
    # ^ []시작 , [^]not, $끝
    # {2,}2글자 이상 
    # ^[a-z0-9]{2,} 소문자 또는 숫자 2글자 이상
    # .[a-z]{2,}$    . 후에 소문자영자로 시작해서 2글자 이상으로 끝난다.
    exp=re.findall('^[a-z0-9]{2,}@[a-z0-9]{2,}\.[a-z]{2,}$',email)
    if len(exp) == 0:
        print(email, '잘못된 이메일 형식')
        return

    print(email,'올바른 이메일 주소')    
    return

email_check('k88im@gmail.co')
email_check('kim_gmail.com')
email_check('kim')
email_check('kim@gmail.com')

print('-'*30)
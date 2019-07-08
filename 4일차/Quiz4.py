# 1. 반복문, 조건문, 함수를 활용하여 주어진 정수 리스트의 최대값을 출력하는 함수를 만들어보세요.
# 주어진 함수는 주어진 리스트 A 를 입력값으로 받습니다.
# if문의 적절한 조건을 추가해 봅시다. (max와 리스트내의 값들을 순서대로 비교)
# 리스트의 값이 max보다 클 때 max를 그 리스트의 값으로 바꿉니다.

def maxFunc(mlist) :
    max = 0
    for i in mlist :
        if max < i:
            max = i
    return max

A = [1, 2, 3, 4, 5, 6, 73, 8, 10, 54]
maxNum = maxFunc(A)
print (maxNum)


# 2. 다음 조건에 맞는 함수를 작성해보세요.
# 함수의 이름은 자유롭게 정합니다.
# a, b를 입력값으로 받습니다.
# 함수 내에서 list 자료형에 a + b, a - b, a * b를 저장한다.
# 위에서 저장한 list 를 리턴합니다.

def cal(a,b) :
    mlist = [a+b,a-b,a*b]
    return mlist
print(cal(2,3))

# 3. 한 개 또는 두 개의 숫자 인자를 전달받아,
# 하나가 오면 제곱, 두개를 받으면 두 수의 곱을 반환해주는 함수를 정의하고 사용해본다.

def cal2(a,b=False) :
    num = 0
    if b is not False :
        num = a*b
    else : num = a* a
    return num
print(cal2(3,1))
print(cal2(3))

def calc(*args):
    num = len(args)
    if not(num ==1 or num ==2):
        raise ValueError('인자는 1개나 2개만 입력하셈')
    if num == 1:
        return args[0] ** 2
    elif num == 2:
        return args[0] * args[1]

print(calc(3,1))
print(calc(3))

def calc2(x, y =None) :
    return x * (y if y else x)

print(calc2(3,1))
print(calc2(3))

# 4. 매개변수로 문자열을 받고, 해당 문자열이 red면 apple을,
# yellow면 banana를, green이면 melon을, 어떤 경우도 아닐 경우
# I don’t know를 리턴하는 함수를 정의하고,
# 이 함수를 사용하여 result 변수에 결과를 할당하고 print 해본다.

def chk(str):
    if str == 'red' :
        return 'apple'
    elif str == 'yellow' :
        return 'banana'
    elif str == 'green' :
        return 'melon'
    else :
        return 'I don’t know'
result = chk('yellow')
print(result)
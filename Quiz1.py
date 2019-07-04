# 1. 화면에 "Hello World!"를 출력하세요.
print('"Hello World!"')


# 2. 화면에 "I don't like C language"를 출력하세요.
print('"I don\'t like C language"')


# 3. print 함수를 사용하여 3.1415의 값을 출력하세요.
# 단, 소수점 아래는 첫 번째 자리까지만 표시되도록 하세요.
pi = 3.1415
print('%.1f' % pi)

# 4. 문자열 '720'를 정수형으로 변환하세요. 정수 100을 문자열 '100'으로 변환하세요.
a = '720'
print(int(a), type(int(a)))
a = 100
str(100)


# 5. 2와 4 숫자를 변수에 넣고, 두 변수를 더한 값, 곱한 값, 나눈 값을 출력하세요.
a , b = (2,4)
print(a+b,a*b,a/b)


# 6. 사용자로부터 두 개의 숫자를 입력받은 후 두 개의 숫자를 더한 값, 곱한 값을 각각 출력하는 프로그램을 작성하세요
a = input()
b = input()
print(int(a)+int(b),int(a)*int(b))
print(int(a)+int(b),int(a)*int(b))

# 7. 'niceman', 'google.com' 문자열을 연속해서 출력할때 구분자를 @으로 변경하여 출력하세요.
a = 'niceman'
b = 'google.com'

print(a,b,sep='@')


#8. str = 'Niceboy' 이 변수를 이용해서 아래와 같은 결과가 나오도록 슬라이싱하여 출력하세요.

'''
Nic
Niceboy
Nicebo
Niceboy
ie
bo
iceb
yobeciN
Ncby
'''
str = 'Niceboy'
l = list(str)
l.reverse()
print(str[:3],str[:],str[:-1],str[:],str[1:2]+str[3:4],str[4:6],str[1:5],''.join(l),str[::2],sep="\n")
print(''.join(l),str[::-1],sep="\n")


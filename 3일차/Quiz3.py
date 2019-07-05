# 파이썬 흐름제어(제어문)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
for key in q1:
    if key == '가을':
        print(q1[key])

print([q1[s] for s in q1 if s == '가을'])
print(''.join([q1[s] for s in q1 if s == '가을']))
# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.(키 또는 값 모두 확인)
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
for key, val in q2.items():
    if key  == '사과' or val == '사과':
        print('있음')
        break
else : print('없음')


# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점
score = 75
if 80 < score : print('A 학점')
elif 60 < score : print('B 학점')
elif 40 < score : print('C 학점')
elif 20 < score : print('D 학점')
else : print('E 학점')

# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
val = [12,6,18]
max = val[0]
for i in val :
    if max < i : max = i
print(max)

# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
id = 1234567
flag = int(id/1000000)
if flag == 1 or 3 : print('남자')
elif flag == 2 or 4 : print('여자')

# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]
for i in q3 :
    if i == '정' : continue
    print(i)

print(' '.join([s for s in q3 if s != '정']))

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
for i in range(1,101) :
    if i % 2 : print(i, end=' ')
print('')
print(' '.join([str(s) for s in range(1,101) if int(s%2) ]))
# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]

for i in q4:
    if len(i) >= 5 : print(i)

print([s for s in q4 if len(s) >= 5])

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for i in q5:
    if ord(i) >= ord('a') : print(i)

# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for i in q6 :
    if ord(i) < ord('Z') : print(i.lower(), end=' ')
    else : print(i.upper(), end=' ')

for i in q6 :
    if i.islower() : print(i.upper(), end=' ')
    else : print(i.lower(), end=' ')

print([s.upper() if s.islower() else s.lower() for s in q6])
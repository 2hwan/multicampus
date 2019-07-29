# 파일 입출력
# input('Message')
# f = open('파일경로','파일접근모드', encoding='utf-8')
# f.write('데이터')
# f.close()
# 접근모드 r:읽기, w:쓰기 ,a:추가

f = open('data/test.txt','w',encoding='utf-8')
for i in range(1,11):
    data = '%d번째 줄입니다.\n' % i
    f.writelines(data) # line들의 list를 넘긴다
f.close()

f = open('data/test.txt','a') # append
f.write('-'*50)
for i in range(1,21):
    data = '\n %d : Hello Python ' %i
    f.write(data)
f.write('\n'+'-'*50)
f.close()

f = open('data/test.txt','r', encoding='utf-8')
data = f.read() #한번에 다읽음, 파일 사이즈가 크면 못읽음
print(data)
data = f.read()
print('두번째' + data + '종료')
f.seek(0, 0) # 파일 핸들러
data = f.read()
print(data)
f.close()

f = open('data/test.txt','r', encoding='utf-8')
while 1 :
    data = f.readline()
    print(data, end='')
    if not data : break
f.close()

f = open('data/test.txt','r', encoding='utf-8')
data = f.readlines() #리스트에 담음
for i in data :
    print(i, end='')
f.close()

# with 문 이용하기
f = open('data/foo.txt','w')
f.write('Life is too short, you need python')
f.close()

with open('data/foo.txt','w') as f : # close 안써도 되는 with 문
    f.write('Life is too short, you need python')

with open('data/test2.txt', 'w', encoding='utf-8') as f :
    for i in range(1, 11) :
        data = '%d번째 줄 입니다 \n' % i
        f.write(data)

with open('data/test2.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    print(data)

with open('./data/test4.txt','w') as f: #프린트를 이용해 파일에 쓸 수 있음
    print('Test Contents!',file =f)
    print('Test Contents!!', file=f)




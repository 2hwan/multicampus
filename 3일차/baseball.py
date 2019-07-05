#야구
import random

com = set()

while 1 :
    com.add(random.randint(1,9))
    if len(com) == 3 : break

print(com)
com = list(com)
print('*'*20)
cnt = 0
while 1:
    val = input('숫자 세개 입력 : ')
    myval = [int(i) for i in val]

    out = 0
    strike = 0
    ball = 0

    for i in range(0,3) :
        for j in range(0, 3) :
            if com[i] == myval[i] :
                strike += 1
                break
            elif (com[i] == myval[j]) and (i != j) :
                ball += 1
                break
    out = 3 - strike - ball
    print('Strike : %d, Ball : %d, Out : %d '% (strike,ball,out))
    cnt += 1
    if strike == 3 :
        print('*' * 20)
        print('%d 번 만에 정답!!'% (cnt))
        break



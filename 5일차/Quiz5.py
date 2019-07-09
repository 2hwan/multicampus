# with 구분을 사용해서 작성하세요

# 1. 50~100 사이의 난수 5개를 생성해서 score.txt 파일을 생성하세요.
import random

with open('data/score.txt', 'w', encoding='utf-8') as f :
    for i in range(1,6) :
        f.write(str(random.randint(50, 100)) + '\n')

# 2. score.txt 파일을 생성한 후 평균을 소숫점3자리까지 표현하세요.
# 95
# 78
# 92
# 89
# 100
# 66
with open('data/score.txt', 'r', encoding='utf-8') as f:
    score = f.readlines() # 리스트로 온다
    print(score)
    sum = 0
    for i in score :
        sum += eval(i)
    print('%.3f' % float(sum/len(score)))


# sum = 0
# num = data.split('\n')
# for i in range(1,5) :
#     sum += int(num[i])
# print('%.3f' % float(sum/5))


# 3. 다음 소스 코드에서 클래스를 작성하여
# 게임 캐릭터의 능력치와 '베기'가 출력되게 만드세요.
class Knight():
     def __init__(self, health, mana, armor):
         self.health = health
         self.mana = mana
         self.armor = armor
     def slash(self):
         print('베기')


x = Knight(health=542.4, mana=210.3, armor=38)
print(x.health, x.mana, x.armor)
x.slash()

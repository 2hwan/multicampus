#연습문제 Q1
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self,val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)

#Q2
class MaxLimitCalculator(Calculator):
    def add(self,val):
        self.value += val
        if self.value > 100 : self.value = 100

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)

#Q3
print(all([1, 2, abs(-3)-3])) #0 이있으면 False
print(chr(ord('a')) == 'a')

#Q4
mlist = [1, -2, 3, -5, 8, -3]
result = filter(lambda x : x > 0, mlist)
print(list(result))

#Q5
print(hex(234))
print(int(hex(234), 16))

#Q6
arr = [1, 2, 3, 4]
brr = map(lambda x: x * 3, arr)
print(list(brr))

#Q7
mlist = [-8, 2, 7, 5 ,-3, 5 ,0 ,1]
print(max(mlist) + min(mlist))

#Q8
print(round(17/3,4))

#Q10
import os

if not os.path.isdir('C:\doit'):
    os.mkdir('C:\doit')

os.chdir('C:\doit')
os.system('dir')
f = os.popen('dir')
print(f.read())

#Q11
import glob

print(glob.glob('C:\doit\*.py'))

#Q12
from datetime import datetime
now = datetime.now()
print(now.strftime('%Y/%m/%d %H:%M:%S'))

#Q13
import random
k = range(1, 45)
com = random.sample(k, 6)
print(com)
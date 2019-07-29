import random

n = random.randint(1,100)
print(n)
while 1:
    ans = input("Guess my number (1~100)? (Q to EXIT) :")
    if ans.upper() == 'Q':
        break
    ans = int(ans)
    if n == ans :
        print("Correct!")
        break
    elif n > ans :
        print('UP!')
    else : print('DOWN!')
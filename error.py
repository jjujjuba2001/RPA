try:
    age = int(input('나이를 입력 : '))
except:
        print('입력이 정확하지 않슴돠. 다시 입력해 주세요.')
        #while age is not type(int):
        #age = int(input('나이를 입력 : '))
else:
    if age <= 18:
        print('미성년자 출입금지')
    else:
        print('환영합니다.')


import random

def rando (a):
     num = random.choice(a)
     a.remove(num)
     return num

li = [44,222,6456,322,13]

print(rando(li))

print (random.sample(li,3))

print (li)

sorted()
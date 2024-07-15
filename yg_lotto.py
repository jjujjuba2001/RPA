import random

jo_num = []   # 조 번호 리스트
num = []      # 나머지 번호 리스트

print ('연금 복권 번호 추출을 시작 합니다.')
print ('=' * 50)

for i in range(5):
    jo_num.append(random.randrange(1,6)) # 중복 체크 불필요
    '''while num in result:
        num = random.randrange(1,46)
    result.append(num)'''
    for n in range(6):
        num.append(random.randrange(0,10))  # 중복 체크 불필요

    '''while num in result:
        num = random.randrange(1,46)
    result.append(num)'''

print (jo_num)
print (num)

for j in range(5):
    print ()
    print ("%s 조 " % jo_num[j], end=" ")  # 조 번호 표시

    for k in range(6):
        print (num.pop(), end=" ")  # 나머지 번호 리스트에서 하나씩 꺼내서 보여주기

print ()
print ('=' * 50)

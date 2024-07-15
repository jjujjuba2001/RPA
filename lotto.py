import random

result = []

print ('로또 번호 추출을 시작 합니다.')
print ('=' * 50)

for i in range(7):
    num = random.randrange(1,46)
    while num in result:
        num = random.randrange(1,46)
    result.append(num)


for j in range(7):
    if result[j] == result[5]:
        print (result[j], end=' ')
        
    elif result[j] == result[6]:
        print ("보너스 번호 : ", result[j])
        
    else:    
        print (result[j], end= ', ')

print ('=' * 50)

            
        
import random

result = []

print ('로또 번호 추출을 시작 합니다.')
print ('=' * 50)

for i in range(7):
    num = random.randrange(1,46)
    while num in result:                   # 중복 숫자 제거하기, 리스트 안에 num 이 있다면 다시 뽑기
        num = random.randrange(1,46)
    result.append(num)


for j in range(7):
    if result[j] == result[5]:
        print (result[j], end=' ')             # 보너스 번호 전에는 공백 출력하기
        
    elif result[j] == result[6]:
        print ("보너스 번호 : ", result[j])    # 보너스 번호 구분해 출력하기
        break
    else:    
        print (result[j], end= ', ')         # 가로 한줄 , 로 구분해 출력하기

print ('=' * 50)

            
        

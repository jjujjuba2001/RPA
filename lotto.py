import random

result = []

print ('로또 번호 추출을 시작 합니다.')
print ('=' * 50)

for k in range(5):
    for i in range(7):
        num = random.randrange(1,46)
        while num in result:                   # 중복 숫자 제거하기, 리스트 안에 num 이 있다면 다시 뽑기
            num = random.randrange(1,46)
        result.append(num)
print(result)

for a in range(5):
    j = 0
    for j in range(7):
        if j == 5:
            print (result.pop(), end=' ')             # 보너스 번호 전에는 공백 출력하기
        
        elif j == 6:
            print ("보너스 번호 : ", result.pop())    # 보너스 번호 구분해 출력하기
            break
        else:    
            print (result.pop(), end= ', ')         # 가로 한줄 , 로 구분해 출력하기

print ('=' * 50)
        
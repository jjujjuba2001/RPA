# 주민번호로 성별 판별 하기

pin = '881120-4068234'

pin = pin.replace('-4','-3')
if pin[7] == "1" or pin[7] == "3":
         print("남자")
elif pin[7] == "2" or pin[7] == "4":
        print ("여자")
else:
        print("없음")

print(pin)

# 나무 열번 찍기 (while 브레이크)
treehit = 0
while treehit <10:
    treehit = treehit + 1
    print("나무를 %d 번 찍었습니다." % treehit)
    if treehit == 10:
        print ('나무 넘어감')

# 커피 자판기 (while 브레이크)

'''coffee = 10

while True:
       money = int(input("돈을 넣어 주세요 : "))
       if money == 300:
              print('커피 나갑니다.')
              coffee -= 1
       elif money > 300:
              print('거스름돈 %d를 주고, 커피도 줍니다.' % (money-300))
              coffee -= 1
       else:
              print('돈을 돌려주고, 커피도 주지 않습니다.\n남은 커피의 양은 %d 개 입니다.' % coffee)
       if coffee == 0:
              print('커피 다 떨어짐. 판매 중지')
              break'''
       
# 10 까지 수 중 홀수만 출력 하기
num = 0

while num < 10:
    num += 1
    if num%2 == 0:
        continue
    else :
        print (num)


# 10 까지 수 중 3의 배수를 뺸 나머지 출력 하기
num = 0

while num < 10:
    num += 1
    if num%3 == 0:
        continue
    else :
        print (num)





# 학생 성적별 합격 여부 (for 문)

num =0
stu = [75,55,60,59,100]
for i in stu:
    num += 1
    if i >= 60:
        print ('%d 번째 학생은 합격입니다.' %num)
    else:
        print ('%d 번째 학생은 불합격입니다.' %num)

speci = ('=') * 50
print (speci)

# 학생 성적별 합격 여부 (for continue 추가)

num =0
stu = [75,55,60,59,100]
for i in stu:
    num += 1
    if i >= 60:
        print ('%d 번째 학생은 합격입니다.' %num)
    else:
        continue
        print ('%d 번째 학생은 불합격입니다.' %num)

speci = ('=') * 50
print (speci)

# 학생 성적별 합격 여부 (for range 추가)

num = 0
for i in range(len(stu)):
    if stu[i] < 60:
        continue # 60점 미만 메시지 생략
    print('%d 번 학생 축하합니다. 합격입니다.' % (i+1))


speci = ('=') * 50
print (speci)

# 1 ~ 100 까지 합 구하기 (for 문)

num =0
for i in range (1,101):
    num += i
    if i == 100:
        print('%d' % num)

speci = ('=') * 50
print (speci)

# 구구단 (for 문)

for i in range (2,10):
    print('%d 단 :' %i, end = " ")
    for j in range (1,10):
        print(i * j, end = " ")
    print (' ')

speci = ('=') * 50
print (speci)

# 구구단 (for 문 리스트 커프리헨션)

result = [x * y for x in range(2,10)
                for y in range(1,10)]
print (result)
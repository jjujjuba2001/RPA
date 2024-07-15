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


speci = ('=') * 50
print (speci)

# 학생 성적 평균 내기 (for 문 )

stu = [70,60,55,75,95,90,80,80,85,100]
total = 0

for i in range(len(stu)):
    print ('%d 번 학생 성적은 %d 입니다.' %(i+1, stu[i]))
    total += stu[i]
    print ('총합은 %d 입니다.' %total)

aver = total / len(stu)
print ('학생 성적의 평균은 : %0.1f 입니다.'% aver)

speci = ('=') * 50
print (speci)

# 별 표시 하기 (for 문 )

i = 0
while True:
    i += 1
    if i > 5: break
    print('*' * i)

def multi (choice, *args):
    if choice == 'add':
        result = 0
        for i in args:
            result += i

    elif choice == 'sub':
        result = 0
        for i in args:
            result -= i

    elif choice == 'mul':
        result = 1
        for i in args:
            result *= i

    elif choice == 'dib':
        result = 1
        for i in args:
            result /= i
    return result


print (multi('add', 7,8,56,4,3,2,1))
print (multi('sub', 7,8,56,4,3,2,1))
print (multi('mul', 7,8,56,4,3,2,1))
print (multi('dib', 7,8,56,4,3,2,1))

'''f = open("C:\doit\복습.txt", "w")

for i in range (1,11):
        data = "%d 번째 줄 입니다.\n" %i
        f.write(data)

f.close()'''

f = open ("C:\doit\복습.txt", "r")
lines = f.readlines()
for line in lines:
    line = line.strip()
    print(line)

f.close()

import sys
args = sys.argv[1:]
for i in args:
    print(i)

    
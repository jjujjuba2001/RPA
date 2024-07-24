def aver (*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

a = aver (1,2)
print (a)

b = aver (1,2,3,4,5)
print (b)


'''input1 = input("첫 번째 숫자를 입력하세요 : ")
input2 = input("두 번째 숫자를 입력하세요 : ")

total = int(input1) + int(input2)
print ('두 수의 합은 %d 입니다.' % total)'''

'''f1 = open (r"C:\doit\test.txt", "w")
f1.write ("life is too short. \nyou need python.")
f1.close()

f2 = open (r"C:\doit\test.txt", "r")
print (f2.read())
f2.close()'''


'''user_input = input("저장할 내용을 입력하세요 : ")
f = open (r"C:\doit\test.txt", "a")
f.write("\n")
f.write(user_input)
f.close()'''

f = open (r"C:\doit\test.txt", "r")
body = f.read()
f.close()
print (body)

body = body.replace ("python", "java")
f = open (r"C:\doit\test.txt", "w")
f.write(body)
f.close()


import sys



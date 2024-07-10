#do it chap 1
print('hello world')
a = 'hello'
a
print(a)

name = 'gil dong'
age = 33

print(f"나의 이름은 {name*2} 입니다. 나이는 {age+3} 입니ㅏㄷ.")

d = {'name' : 'hong', 'age' : 30, 'adress' : 'suown'}
print(f"my name is {d["name"]} 입니다. 나이는 {d['age']} 입니ㅏㄷ.{d['adress']}")

print(f'{"hi":>15}')
print(f"{"hi":+^15}")
print(f"{"python":!^12}")

a = "hobby"
#e = a.count('b')
print(a.count('===='))

b = "    python is the best choice      .       "
print(b.count('b'))
print(b.find('y'))
print(b.find('k'))
print("+".join(b))
print("+".join(['a','b','c','d']))
print(b.upper())
print(b.lower())
print(b.strip())
print(b.replace("python", "excel"))
print(b)
'''a = 123
b = -123
c = 0
print(str(a) + "," + str(b),str(c))

a= 0o177
print(a)

x = 2

#a = 10*18**x
#b = 2*11

print (a+b)'''

a= 14//3
b= 14%3
print ("몫 : " + str(a) + ", " +"나머지 : " + str(b))

print ('\"it\'s list so fast.\"')

a = "\"life is too short\"\n you need python."
print(a)

b = '''
life is too short
you need python.\a
    '''

print(len(a))
c= a[:5]
print(c)
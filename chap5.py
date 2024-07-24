class fourcal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add (self):
        result = self.first + self.second
        return result
    
    def sub (self):
        result = self.first - self.second
        return result

    def mul (self):
        result = self.first * self.second
        return result

    def div (self):
        result = self.first / self.second
        return result


a = fourcal()
b= fourcal()

a.setdata(3,9)
b.setdata(5,10)

print (a.first)     
print (a.second)
print ('=' * 50)     
print (b.first)     
print (b.second)
print ('=' * 50) 
print (a.mul())
print (b.div())


class sung:
        def __init__(self, first, second):
            self.first = first
            self.second = second

        def cla (self):
            if self.second > 70:
                print ("%s 과목은 %d 점으로 평균 이상입니다." % (self.first, self.second))
            else:
                print ("%s 과목은 %d 점으로 평균 이하입니다."% (self.first, self.second))

c = sung("영어", 70)
c.cla()
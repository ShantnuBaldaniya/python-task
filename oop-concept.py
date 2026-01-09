##  Encapsulation

class bank:
    
    def __init__(self,balance):
        self.__balance=balance
    def show_balance(self):
        print('bank balance =',self.__balance)
    def deposite(self,amount):
        self.__balance+=amount
        
b=bank(5000000000)
b.show_balance()
b.deposite(99)
b.show_balance()


class atmaccount:
    
    def __init__(self):
        self.__pin = 8586
        self.__balance = 202020202

    def check_pin(self, pin):
        user = int(input('enter the pin for show balance and deposite = '))
        if user == self.__pin:      
            return True
        else:
            return False

    def show_balance(self, pin):
        if self.check_pin(pin):
            print('your balance is =', self.__balance)
        else:
            print('invalid pin')

    def deposite(self, pin, amount):     
        if self.check_pin(pin):
            self.__balance += amount
            print('deposit successful')
        else:
            print('deposit failed')


c = atmaccount()

c.show_balance(8586)
c.deposite(8586, 99999)
c.show_balance(8586)


                                ## Inheritance ###
                
class account:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        
class show_baldance(account):
    def show_balance(self):
        print('the balance  is =',self.balance)
    def name_show(self):
        print('name is =',self.name)

d=show_baldance('shantnu',3939393)
d.show_balance()
d.name_show()
        

    
                                            ### polymorphism ###
                                            
class Animal:
    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"


animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.sound())
    
    
    
class student:
    def __init__(self,name,rollnumber,marks):
        self.name=name
        self.rollnumber=rollnumber
        self.marks=marks
    
    def student_name(self):
        return self.name
    def student_rollnumber(self):
        return self.rollnumber
    def student_marks(self):
        
        return self.marks
    
s=student('shantu',33,23)     
print('name',s.student_name())
print('no=',s.student_rollnumber())
print('marks',s.student_marks())


class bankaccount:
    def __init__(self,accountnumber,holdername,balance):
        self.accountnumber=44535332
        self.holdername='shantnu'
        self.balance=3232
    
    def deposite(self,amount):
        
        self.balance+=amount
        
    def withdraw(self,amount):
        self.balance-=amount
        
    def check_balance(self):
        return self.balance
    
b= bankaccount(4444444,'shantnu',3232)
b.deposite(9999)
b.withdraw(3232)
print(b.check_balance())


class shape:
    def __init__(self,length,width):
        self.lenght=length
        self.width=width
    def calculatearea(self):
        return 2*(self.width+self.lenght)
    # def calculateperimeter(self):
    #     return self.width*self.length
    
r=shape(3,5)
print('area is = ',r.calculatearea())
# print('peremiter is =',r.calculateperimeter())


class employee:
    def __init__(self,id,salary):
        self.__id=id
        self.__salary=salary
    
    def getsalary(self):
        return self.__salary
    
    def setsalary(self,new):
        self.__salary=new 
        return self.__salary
    

e=employee(23232,30000)
print('salary is a =',e.getsalary())
print('after increment=',e.setsalary(34343))
 
class calculator:
    def add(self,a,b,c=None):
    
        if c is None:
            return a+b
        else:
            return a+b+c
        
c=calculator()
print(c.add(2,3))
print(c.add(2.3,5,9.9))
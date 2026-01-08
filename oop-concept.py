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
    


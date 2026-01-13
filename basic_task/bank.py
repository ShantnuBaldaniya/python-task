class bank:
    def __init__(self,balance):
        self.__balance=balance
    
    
    def check_balance(self):
        return self.__balance
    
    def doposite(self,amount):
        self.amount=amount
        
        self.__balance+=amount
        
    def withdraw(self,amount):
        
        self.amount=amount
        
        self.__balance-=amount
        
b=bank(232323)
v=int(input('enter amount for deposite:'))
b.doposite(v)
print('balance after deposite',b.check_balance())
w=int(input('enter amount for withdraw:'))
b.withdraw(w)
print('balance after withdraw',b.check_balance())
print('final balance is ',b.check_balance())


        
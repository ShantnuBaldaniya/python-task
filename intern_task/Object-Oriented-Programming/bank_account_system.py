class Account:
    def __init__(self,ac_num,holder_name,balance):
        self.ac_num=ac_num
        self.holder_name=holder_name
        self.balance=balance
    def deposite(self,amount):
        if amount>0:
            self.balance+= amount
            return ('after deposite  balance is:',self.balance)
        else:
            return ('enter amount postive')
    
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            return ('succes withdraw after balance is:',self.balance)
        else:
            return ('insufficient balance')
        
    def get_balance(self):
        return ('your final balance is',self.balance)

class SavingAccount(Account):
    def __init__(self,ac_num,holder_name,balance,interest_rate=0.07):
        self.interest_rate=interest_rate
        super().__init__(ac_num,holder_name,balance)
        
    def calculate_interest(self):
        I=self.balance*self.interest_rate
        self.balance+=I
        print('your balance is after int:',self.balance)
        
        
    
class CurrentAccount(Account):
    def __init__(self,ac_num,holder_name,balance,overdraft=300000):
        super().__init__(ac_num,holder_name,balance)
        self.overdraft=overdraft
    
    def withdraw(self,amount):
        
        if amount<self.balance+self.overdraft:
            self.balance-=amount
            return('withdraw succ balance is:',self.balance)
        else:
            print('sorry!,your limit has been over')
            
a=Account(1234,'shantnu',303030)
s=SavingAccount(1234,'shantnu',303030)
c=CurrentAccount(1234,'shantnu',3030,303)

print(a.deposite(3))
print(a.get_balance())

s.calculate_interest()
c.withdraw(33333)

        
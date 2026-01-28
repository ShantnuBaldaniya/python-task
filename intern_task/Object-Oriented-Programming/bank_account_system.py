class Account:
    def __init__(self,ac_num,holder_name,balance):
        self.ac_num=ac_num
        self.holder_name=holder_name
        self.balance=balance
    def deposite(self,amount):
        if amount>0:
            return ('new balance is:',self.balance+amount)
        else:
            return ('enter amount postive')
    
    def withdraw(self,amount):
        if amount<=self.balance:
            return ('succes withdraw',self.balance-amount)
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
        print('your baalnce is after int:',self.balance)
        
        
    
class CurrentAccount(Account):
    def __init__(self,ac_num,holder_name,balance):
        super().__init__(ac_num,holder_name,balance)
    
    def withdraw(self,balance,overdraft=300000):
        
        s
        
        
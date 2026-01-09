import random

class BankAccount:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposite(self, amount):
        self.balance = amount + self.balance

    def withdraw(self, amount):
        self.balance -= amount

    def check_balance(self):
        return self.balance

    def display_details(self):
        return (self.balance, self.holder_name, self.account_number)



dic = {}
n = int(input('enter the how many pair u want: '))

for i in range(n):
    key = input('enter key: ')
    value = input('enter value: ')
    dic[key] = value

    key = input('enter key: ')
    value = input('enter value: ')
    dic[key] = value

    key = 'account number'
    value = random.randint(10000, 99999)
    dic[key] = value

    print(dic)



accounts = {}



c = BankAccount(220760107006, 'shantnu', 232323)

print(
    'enter below service u want\n'
    '0 for create new account\n'
    '1 for deposite\n'
    '2 for withdrwa\n'
    '3 for account details\n'
    '4 for check balance'
)

user = int(input('enter the service number = '))


if user == 0:
    acc_no = random.randint(10000, 99999)
    bal = int(input("enter opening balance: "))

    accounts[acc_no] = bal

    print("account created successfully")
    print("account number:", acc_no)
    print("balance:", bal)
    print("all accounts:", accounts)



elif user == 1:
    print('u chose the deposite plz enter the amount')
    amount = int(input('enter the amount: '))
    c.deposite(amount)
    print('your balance after deposite =', c.check_balance())



elif user == 2:
    print('u chose the withdraw plz enter the amount')
    amount = int(input('enter the amount: '))
    c.withdraw(amount)
    print('your balance after withdraw =', c.check_balance())



elif user == 3:
    print('yout details is:',c.display_details())

else:
     print('your balance is ',c.check_balance())
    



    
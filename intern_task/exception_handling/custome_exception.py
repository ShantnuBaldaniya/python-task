class AgeError(Exception):
    pass

age=int(input('enter the age:'))
try:
    if age<18:
        raise AgeError('enter the age above 18')
    else:
        print('u can vote')
except AgeError as e:
    print(e)
    
    
class InsufficientFundsError(Exception):
    pass

try:
    def withdraw(amount,balance):
        if amount>balance:
            
            raise InsufficientFundsError('sorry! your balance is a lower')
        return balance-amount 
    
    b=int(input('etnter the balance:'))
    amount=int(input('enter the withdraw amount:'))
    
    n=withdraw(amount,b)
    print(n)
except InsufficientFundsError as e:
    print(e)
        


class DuplicateEntryError(Exception):
    pass

def find(user,list1):
    if user in list1:
        raise DuplicateEntryError('this is name are already in the database!')
    list1.append(user)
    return 'succsess'
   
try:
    list1=['shntnu','ahir']
    name=input('enter the name :')
    n=find(name,list1)
    print(list1)
except DuplicateEntryError as e:
    print(e)
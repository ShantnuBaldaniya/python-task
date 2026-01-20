class Calculator:
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        if b==0:
            print('not divisible by zero')
        else:
            return a/b
    
c=Calculator()
print('the addition is: ',Calculator.add(12.32,32))
print('the substraction is: ',Calculator.sub(12.32,32.32))
print('the multiplication  is: ',Calculator.mul(12.32,32))
print('this is div:',Calculator.div(1,0))
            

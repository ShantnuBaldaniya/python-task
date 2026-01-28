try:
    def fact(num):
        if num==0:
            return 1
        return num*fact(num-1)
    num=int(input('Enter the num for factorial:'))
    print(fact(num)) 
except :
    print(' sorry! enter the postive number only !')
    

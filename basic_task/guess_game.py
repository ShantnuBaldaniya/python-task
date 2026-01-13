import random
number=random.randint(1,99)
user=None

    
while(user!=number):
    print(number)
    user=int(input('enter the number to guess:'))
    if user==number:
        print('u win the game')
    elif user>number:
        print('less your guess')
    elif user<number:
        print('too low ')
    else:
        print('enter valid number')
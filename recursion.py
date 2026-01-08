 
#Calculate the factorial of a number using recursion.

def factorial(num):
    if num==0:
        return 1
    return num * factorial(num-1)


#Calculate the sum of all elements in a list using recursion.
   
def sum(list):
    if len(list)==0:
        return 0
    return list[0]+sum(list[1:])
list=[1,2,3,4,5,6]
print(sum(list))



#Count the number of elements in a list using recursion

def count_list(lst):
    if len(lst) == 0:     
        return 0
    return 1 + count_list(lst[1:])  

lst = [1, 2, 3, 4, 5]
print(count_list(lst))





#Write a function that checks if a given string is a palindrome (reads the same forwards and backward), ignoring spaces and letter casing.

def palin(string):
    if len(string)>=1:
        return True
    if string[0]!=string[-1]:
        return False
    return palin(string[1:-1])


 #Implement the FizzBuzz game: Print numbers from 1 to n, but for multiples of 3, print "Fizz," for multiples of 5, print "Buzz," and for multiples of both 3 and 5, print "FizzBuzz."
  
def game(user):
    if user == 0:        
        return
    game(user-1)           
    if user % 3 == 0 and user % 5 == 0:
        print('fizzbuzz')
    elif user % 3 == 0:
        print('fizz')
    elif user % 5 == 0:
        print('buzz')
    else:
        print(user)

number = int(input('enter the number = '))
game(number)



#Implement a function that checks if a given year is a leap year

def leap_year(year):
    if year <= 0:    
        return False
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year = int(input("Enter a year: "))
print("Leap year" if leap_year(year) else "Not a leap year")




#Create a simple number guessing game where the program generates a random number, and the user has to guess it

import random
def game_start():
    user=None
    import random
    number=random.randint(1,100)
    attempt=0
    print(number)
    
    while number!=user:
        attempt+=1
        user=int(input('enter the guess='))
        if number>user:
            print('make a gues icrease')
        elif number<user:
            print('less your guess')
        else :
            print(f'u win the game in {attempt} attempt ')
            break
        


#Implement a function that calculates the sum of the digits of a positive integer. 


def digits(number):
    if number==0:
        return 0
    return number%10+digits(number//10)
result=digits(3232323)


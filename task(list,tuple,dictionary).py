                                          ####### list ###############

##1. Given a list of numbers, write a function that takes the list as input and returns a new list 
# containing only the even numbers from the original list.

def even_num(list):
    list1=[]
    for i in list:
        if i%2==0:
            list1.append(i)
    return list1
list=[1,2,3,4,5,6,7,8]
result=even_num(list)
print('even number list is=',result)

""" 2. Create a list of numbers from 1 to 10 and then use a
list comprehension to create a new list containing the squares of these numbers."""


n=10
sq=[i*i for i in range(1,n+1)]
print('3 question==',sq)




"""3. Create a list of names and then write code to sort
    the list alphabetically in descending order."""


list=['abhay','bob','zzz','hiren','karan','nayan']
list.sort(reverse=True)
print('question=',list)



"""
Write a function that takes two lists as input and returns 
a new list containing elements that are common to both input lists (intersection)."""


def common_number():
    list1=[]
    n=int(input('enter the range for list1='))
    for i in range(n):
        
        element=int(input('enter the element='))
        list1.append(element)
        
    list2=[]
    n=int(input('enter the range for list2='))
    for i in range(n):
        
        element1=int(input('enter the element='))
        list2.append(element1)
    
    common=[]
    list=list1+list2
    for i in list:
        if i  in list1 and i in list2 and i not in  common:
            common.append(i)
    return common

c=common_number()
print('the common list is=',c)


"""Write a function that takes a list as input and returns a new 
list with the elements reversed, without using the built-in reverse method."""

def rev(list):
    
    rev=[]
    for i in list:
        rev=[i]+rev
    return rev

list=[1,2,3,4,5,6,7]
print('the rev is=',rev(list))


"""Write a function that takes two lists as input and returns a new list that contains the 
elements that are unique to each list (i.e., not common to both lists)"""

def remove_duplicate():
    list1=[]
    n=int(input('enter the range for list1='))
    for i in range(n):
        
        element=int(input('enter the element='))
        list1.append(element)
        
    list2=[]
    n=int(input('enter the range for list2='))
    for i in range(n):
        
        element1=int(input('enter the element='))
        list2.append(element1)
    
    final=[]
    list=list1+list2
    for i in list:
        if i  not in final:
            final.append(i)
    return final


c=remove_duplicate()
print(c)

                                                #### tuple  ###########

"""Create a function that takes three arguments 
(name, age, city) and returns them as a tuple. Then, call the function and unpack the tuple into separate variables."""

def create_tuple(name,age,city):
    return (name,age,city)

result=create_tuple('shantnu',20,'surat')
print(result)
name,age,city=result
print(name)
print(city)



"""Given two tuples, create a new tuple that
combines elements from both tuples without any duplicates."""

tuple1=('bob',12,'surat')
tuple2=('helo',12,'delhi')
list1=list(tuple1)
list2=list(tuple2)

tuple3=list1+list2
new=[]
for i in tuple3:
    if i not in new:
        new.append(i)
result=tuple(new)
print(result)
print(type(result))


"""reate a tuple of your favorite movies, andthen write code to print 
the first two movies and the last two movies in the tuple."""

movies=('animal','baghban','border','paltan')
print('the first two movie name:',movies[0],'and',movies[1])
print('the last two movie name:',movies[-1],movies[-2])


"""Write a program that asks the user to enter their
name, age, and city, and then packs these values into a tuple and prints it."""

name = input("Enter your name= ")
age = int(input("Enter your age= "))
city = input("Enter your city= ")

student = (name, age, city)

print("Tuple:", student)

"""
Given three tuples, concatenatethem into a single
tuple while maintaining their original order."""

tuple1 = (1, 2, 3)
tuple2 = (4, 5)
tuple3 = (6, 7, 8)

result = tuple1 + tuple2 + tuple3
print(result)

                                                ######## Dictionary #######


"""Write a function that takes a dictionary of student names and their
corresponding scores as input and returns the name of the student with the highest score.
"""

def top_student(scores):
    highest = 0
    topper = ""

    for name, score in scores.items():
        if score > highest:
            highest = score
            topper = name

    return topper
student={
    'shantnu':85,
    'karan':9
    
}
result=top_student(student)
print(result)


"""Given a list of names, create a dictionary where the keys are the names, 
and the values are the lengths of the names, using a dictionary comprehension"""

d = {'shantnu', 'karan', 'mandeep', 'krunal'}


name_lengths = [(name, len(name)) for name in d]
print(name_lengths)



"""Given two dictionaries, merge them into a new dictionary,
and in case of overlapping keys, combine their values into a list."""

d1={'a':1,'b':2,'c':3}
d2={'b':1,'c':2,'d':3}
merged={}
for k in (d1,d2):
    
    for key ,value in k.items():
        #print(k.items())
        
        if key in merged:
            merged[key].append(value)
        else:
            merged[key]=[value]
print(merged)


"""Create a dictionary of products and their prices. 
Write a program that asks the user for a product name and checks if it exists in the dictionary. If it does, print its price; otherwise, display an error message."""

prices = {
    "laptop": 800,
    "mouse": 25,
    "keyboard": 50
}

user=input('enter a the product name =')
for key,value in prices.items():
    if user==key:
        print('prices is ',value)
        break
else:
    print('error')
    
    
 """Write a function that takes two dictionaries as input and returns
 a new dictionary containing key-value pairs that exist in both input dictionaries.
"""   
    
def common_dict(dic1, dic2):
    common = []
    for key in dic1:
        if key in dic2:
            common.append(key)
        
    return common
dic1 = {"a": 1, "b": 2, "c": 3}
dic2 = {"b": 5, "c": 6, "d": 7}

print(common_dict(dic1, dic2))

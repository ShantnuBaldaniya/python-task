# class student:
#     def __init__(self):
#         print('constructor is called:')
        
# d=student()
# print(d)


# try:
#     a=10
#     b=0
#     print(a/b)
# except Exception as e:
#     print('error',e)
    

# class car:
#     def __init__(self,color,model):
#         self.color=color
#         self.model=model
#     def start(self):
#         print(self.color,self.model,'car is on the way')
# c=car('white','bmw')
# c.start()
        
# class bank:
#     def __init__(self,balance):
#         self.__balance=balance
    
#     def check_balance(self):
#         return self.__balance

# b=bank(300000)
# print(b.check_balance())        


# class A:
#     def show(self):
#         print("A")

# class B(A):
#     def show(self):
#         print("B")

# class C(A):
#     def show(self):
#         print("C")

# class D(B, C):
#     pass

# d = D()
# d.show()


# # class Demo:
# #     def __init__(self,x):
# #         self.x = x
# #         print (self.x) 
# # d = Demo(10)  



# # a = [1,2,3]
# # b = [1,2,3]

# # print(a == b)
# # print(a is b) 
# class A:
#     def show(self):
#         print("A")

# class B:
#     def show(self):
#         print("B")

# def call(obj):
#     obj.show()

# call(A())
# call(B()) 


# class A:
#     def show(self):
#         print("A")

# class B(A):
#     def show(self):
#         print("B")

# class C(A):
#     def show(self):
#         print("C")

# class D(B, C):
#     pass

# d = D()
# d.show() 
# print(D.mro())

# class a:
#     def __init__(self):
#         print('a')
# class b(a):
#     def __init__(self):
#         print('b')
# class c(b):
#     def __init__(self):
#         print('c')
    
# d=a()


# def f():
#     try:
#         return 1
#     finally:
#         return 2

# print(f())

# # try:
# #     file=open('a.txt','r')
# #     data=file.read()
# # except Exception as e:


# # def foo():
# #     print("|                  ","Hello","                   |")
# #     print("|--------------------------------------------|")
# # print("|--------------------------------------------|")
# # print("|","    ",foo," |")
# # print("|--------------------------------------------|")
# # print("|                   ",foo(),"                   |")
# # print("|--------------------------------------------|")

# class student:
#     def __init__(slef,name,age):
#         slef.name=name
#         slef.age=age
#     def display(slef):
#         print('Name:',slef.name)
#         print('Age:',slef.age)
        
# c=student('shantnu',12)
# c.display()
        
    
# class bankaccount:
#     def __init__(self,balance):
#         self.__balance=balance
        
#     def withdraw(self,amount):
#         self.__balance-=amount
#         return ('after the withdraw amount is ',self.__balance)
    
#     def deposite(self,amount):
#         self.__balance+=amount
#         return ('after the deposite amoutn is', self.__balance)
#     def check_balance(self):
#         return self.__balance

# b=bankaccount(303030)
# print(b.withdraw(34343)
# ,b.deposite(9))
# print(b.check_balance())


# class employee:
#     def __init__(self,salary):
#         self.salary=salary
#     def show(self):
#         return ('salary is:',self.salary)
# class manager(employee):
#     def __init__(self,amount,salary):
#         super().__init__(salary)
#         self.amount=amount
       
#     def total(self):
#         return self.salary+self.amount

# c=manager(34000,3030)
# c.show()

# print(c.total())

# class Student:
#     def __init__(self, name):
#         self.name = name

# s = Student("Amit")
# print(s.name)

# class Demo:
#     def show(self):
#         print("Hello")

# d = Demo()
# d.show()

# class A:
#     def __init__(self):
#         print("A")

# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("B")

# b = B()

# class Test:
#     def show(self):
#         print("Hi")

# t = Test()
# t.show()


# class User:
#     def __init__(self):
#         self.__age = 25
#     def show(self):
#         return self.__age

# u = User()
# print(u.show())

# class A:
#     x = 10

# class B(A):
#     x = 20

# obj = B()
# print(obj.x)
# class Dog:
#     def sound(self):
#         print("Bark")


# class Cat:
#     def sound(self):
#         print("Meow")


# animals = [Dog(), Cat()]

# for a in animals:
#     a.sound()
    
    
# class A:
#     def show(self):
#         print("A")


# class B(A):
#     def show(self):
#         super().show()
#         print("B")


# class C(A):
#     def show(self):
#         print("C")
#         super().show()


# class D(B, C):
#     pass


# d = D()
# d.show()

# class Profile:
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email


#     def show(self):
#         print("User:", self.username)
#         print("Email:", self.email)




# p = Profile("rahul_01", "r@gmail.com")
# p.show()


# class Cart:
#     def __init__(self, items=[]):
#         self.items = items
#     def add_item(self, item):
#         self.items.append(item)
#     def show(self):
#         print(self.items)
# c1 = Cart()
# c2 = Cart()
# c1.add_item("Apple")
# c2.show()


# class A:
#     def process(self):
#         print("Processing A")
# class B(A):
#     def process(self):
#         print("Processing B")
# obj = B()
# obj.process()

# class User:
#     def __init__(self, name):
#         self.name = name


# class Admin(User):
#     def __init__(self, role):
#         super().__init__(role)
#         self.role = role

#     def info(self):
#         print(self.name, self.role)


# a = Admin("manager")
# a.info()


# class A:
#     def show(self):
#         print("A")
# class B(A):
#     def show(self):
#         print("B")
#         super().show()
# class C(A):
#     def show(self):
#         super().show()
#         print("C")
# class D(B, C):
#     def show(self):
#         super().show()
# d = D()
# d.show()


# class Account:
#     def __init__(self, balance):
#         self.__balance = balance

#     def withdraw(self, amount):
#         if amount > self.__balance:
#             print("No money")
#         self.__balance -= amount

#     def show(self):
#         print(self.__balance)


# a = Account(1000)
# a.withdraw(200)
# a.show()


# name='shaannanananatttttuuuuuntnuhhhhhhsssss'
# for i in name:
#     if name.count(i)==1:
#         print(i)
#         break
        
# list1=[1, [2, [3, 4]], 5]
# list2=[]
# for i in list1:
    
#     if type(i)==list:
#         for j in i:
#             list2.append(j)
# print(list2)


age=9
if age>=18:
    print('u can vote')
else:
    print('not')
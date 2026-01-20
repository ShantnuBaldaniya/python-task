def func(x,data=[]):
    data.append(x)
    return data
print(func(3))
print(func(2))


for i in range(3):
    if i==5:
        break
    else:
        print('done')
        
s='python'
s=s[0].upper()+s[1:]
print(s)

a=[1,2,3,4,5]
a[1:4]=[10,20]
print(a)

a=[1,2,3]
b=a
a=a+[4]
b=b+[3]
print(b)
print(a)

x=[1,2,3]
print(id(x)==id(x[:]))


# x=10
# def test():
#     print(x)
#     x=5
# test()

seen=True
reply=False
if seen and not reply:
    print('hello')
    
x=5
y=x
x=10
print(y)

a='hello'
print(a*0)

g=1
if g:
    print('hello')
else:
    print('hi')
    

import numpy as np
 
 
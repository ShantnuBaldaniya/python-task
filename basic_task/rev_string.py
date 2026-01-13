#Write a function to reverse a string without using slicing.
def rev(string):
    rev=''
    for i in string:
        rev+=i
    return rev

string=input('enter the any string')
        
print(rev(string))   
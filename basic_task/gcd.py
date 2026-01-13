def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
a=int(input('enter the 1st number:'))
b=int(input('enter the 2nd number:'))
print('the GCD is:',gcd(a,b))

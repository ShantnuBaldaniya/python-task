number = int(input('enter the range: '))

for i in range(2, number):
    isprime = True
    
    for j in range(2, i):
        if i % j == 0:
            isprime = False
            break
    
    if isprime:
        print(i)



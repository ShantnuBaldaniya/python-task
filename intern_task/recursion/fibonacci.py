def fib(num):
    if num <= 1:
        return num
    return fib(num-1) + fib(num-2)

n = 7  

for i in range(n):
    print(fib(i), end=" ")
    

import time

def timer(func):          
    def wrapper():   
        start = time.time()
        end = time.time()
        print("start fun wrap")     
        start = time.time()
        end = time.time()
        func()
        print(func.__name__,"Time taken:",end - start, "seconds")
        print("start time is:",start)
        print("end time is:",end)
        print("end fun wrap")
    return wrapper
@timer
def add():
    print('decorator is start')
add()
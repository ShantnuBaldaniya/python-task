def memo_cache(func):
    cache = {}   

    def wrapper(x):
        if x in cache:
            print("Cache Used")
            return cache[x]

        print("Calculating")
        result = func(x)
        cache[x] = result
        return result

    return wrapper
@memo_cache
def square(n):
    return n * n

print(square(5))   
print(square(5))   

print(square(6))  

print(square(5454545))
print(square(-5454545))
print(square(54545))
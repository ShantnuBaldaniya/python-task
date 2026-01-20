import math

def pascal(n): 
    for i in range(n):  
        
        print(" " * (n - i), end="")
        for j in range(i + 1):  
            print(math.comb(i, j), end=" ")
        print()  


rows = 5
pascal(rows)

#i = rows j= for number in row


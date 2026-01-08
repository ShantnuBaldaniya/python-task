

"""Create a base class Shape with methods to calculate area and perimeter. 
	Derive classes Circle and Rectangle from it and override the methods"""

class Shape:
    def area(self):
        return 0

    def perimeter(self):
        return 0


class Circle(Shape):
    def area(self, radius):
        return 3.14 * radius * radius

    def perimeter(self, radius):
        return 2 * 3.14 * radius


class Rectangle(Shape):
    def area(self, height, width):
        return height * width

    def perimeter(self, height, width):
        return 2 * (height + width)


"""Create a Calculator class with multiple methods for addition, subtraction, multiplication, and division. 
Implement method overloading to handle different parameter types (int, float, and possibly more). Demonstrate the usage of these overloaded methods"""


class Calculator:
   
    def add(self, a, b):
        return a + b

    
    def subtract(self, a, b):
        return a - b

    
    def multiply(self, a, b):
        return a * b

    
    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b


calc = Calculator()


print(calc.add(5, 3))          # 8
print(calc.subtract(10, 4))    # 6

# Floats
print(calc.multiply(2.5, 4.0)) # 10.0
print(calc.divide(7.5, 2.5))   # 3.0


print(calc.add(5, 2.5))        # 7.5



"""Implement a base class Shape with methods for calculating area and perimeter. Create derived classes such as Circle, Rectangle, 
and Triangle that inherit from Shape and override the relevant methods. Demonstrate polymorphism by creating instances of these classes and calling the area and perimeter methods."""



class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass



class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius



class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        return "Area"

    def perimeter(self):
        return self.a + self.b + self.c



c = Circle(5)
r = Rectangle(4, 6)
t = Triangle(3, 4, 5)

shapes = [c, r, t]

for s in shapes:
    print("Area:", s.area())
    print("Perimeter:", s.perimeter())
    


"""Create a function longest_palindromic_subsequence(s: str) -> int that finds 
the length of the longest palindromic subsequence in a given string."""

def longest_palindromic_subsequence(s):
    def lps(i, j):
        
        if i > j:
            return 0
        if i == j:
            return 1

        
        if s[i] == s[j]:
            return 2 + lps(i+1, j-1)
        else:
            return max(lps(i+1, j), lps(i, j-1))

    return lps(0, len(s)-1)
print(longest_palindromic_subsequence("bbbbabaabbab")) 
print(longest_palindromic_subsequence("cbbd"))   



"""Create a function edit_distance(word1: str, word2: str) -> int that calculates the minimum number of operations (insertion, deletion, or substitution)
required to convert one word into another."""

word1='cat'
word2='cut'
m = len(word1)
n=len(word2)
mat = []

for i in range(m + 1):
    row = []
    for j in range(n + 1):
        row.append(0)
    mat.append(row)

for i in range(m + 1):
    mat[i][0] = i


for j in range(n + 1):
    mat[0][j] = j


for i in range(1, m + 1):
    for j in range(1, n + 1):
        if word1[i - 1] == word2[j - 1]:
            mat[i][j] = mat[i - 1][j - 1]   
            
        else:
            mat[i][j] = 1 + min(
                mat[i - 1][j],     
                mat[i][j - 1],   
                mat[i - 1][j - 1]  
            )
print(mat)




"""Define a function can_partition(nums: List[int], target_sum: int) -> bool that determines whether it is possible to partition a given set of numbers
into two subsets such that the sum of elements in both subsets is equal."""

def can_partition(nums) :
    total = sum(nums)


    if total % 2 != 0:
        return False

    target = total // 2
    possible = {0}   

    for num in nums:
        new_sums = set()
        for s in possible:
            new_sums.add(s + num)
        possible |= new_sums

    return target in possible
result=can_partition([1,2,3,6])
print(result)



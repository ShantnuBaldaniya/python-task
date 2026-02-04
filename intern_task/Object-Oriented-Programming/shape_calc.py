from abc import ABC , abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
        
    @abstractmethod   
    def perimeter(self):
        pass
    

class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return 3.14*(self.radius*self.radius)
    
    def perimeter(self):
        return 2*3.14*self.radius
    
class rec(shape):
    
    def __init__(self,len,wid):
        self.len=len
        self.wid=wid
    
    def area(self):
        return self.len*self.wid
    
    def perimeter(self):
        return 2*(self.len+self.wid)

class tri(shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2   
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5


shap=[circle(3),rec(2,3),tri(1,2,3)]
for i in shap:
    print('area is:',i.area())
    print('permi is :',i.perimeter())
    
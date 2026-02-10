class Bst:
    def __init__(self,r):
        self.r=r
        self.left=None
        self.right=None


    def insert(self, r):
        if r<self.r:
            if self.left:
                self.left.insert(r)
            else:
                self.left = Bst(r)
        else:
            if self.right:
                self.right.insert(r)
            else:
                self.right=Bst(r)

    def search(self, r):
        if self.r == r:
            return True
        elif r < self.r:
            if self.left:
                return self.left.search(r)
            else:
                return False
        else:
            if self.right:
                return self.right.search(r) 
            else:
                return False
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.r)
        if self.right:
            self.right.inorder()
    def delete(self, n):
        if self.left and self.left.r == n:
            self.left = None
        elif self.right and self.right.r == n:
            self.right = None
        else:
            if self.left:
                self.left.delete(n)
            if self.right:
                self.right.delete(n)
                
t=Bst(100)
t.insert(20)
t.insert(30)
t.insert(40)

t.inorder()

print("Search 80:", t.search(80))   
print("Search 10:", t.search(10))   
print("Search 50:", t.search(50))   
print("delete 80")
t.delete(80)
print("Search 80:", t.search(80))

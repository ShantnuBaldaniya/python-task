class Stack:
    def __init__(self):
        self.item=[]
    def push(self,item):
        return self.item.append(item)
    
    def pop(self):
        if self.is_empt():
            return 'stack is empty'
        return self.item.pop()
    def peek(self):
        if self.is_empt():
            return "Stack Empty!"
        return self.item[-1]
    def is_empt(self):
        return len(self.item)==0
    
def rev(text):
    stack=Stack()
    for ch in text:
        stack.push(ch)
    rev=''
    while not stack.is_empt():
        rev+=stack.pop()
    return rev  

c=Stack()
c.push(20)
c.push(30)
c.push(40)
c.pop()

print(c.peek())
print(rev('shantu'))
def bal(text):
    stack=[]
    for ch in text:
        if ch== '(':
            stack.append(ch)
        elif ch==')':
            if len(stack)==0:
                return False
            stack.pop()
    return len(stack)==0
    
print(bal('()())()'))

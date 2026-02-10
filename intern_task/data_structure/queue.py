class Q:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Q is Empty!"
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            return "Q is Empty!"
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

q = Q()

q.enqueue('task 1 done')
q.enqueue('task 2 done')
q.enqueue('task 3 done')
print('task start')
while not q.is_empty():
    task=q.dequeue()
    print(task)
print('all task done' )

# print("1st ele is:", q.front())    
# print("remove element after:", q.dequeue()) 
# print("Size:", q.size())      
# print("1st element is :", q.front())     
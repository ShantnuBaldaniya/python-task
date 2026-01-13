class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, item):
        self.q.append(item)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            return self.q.pop(0)

    def is_empty(self):
        if self.q == []:
            return True
        else:
            return False
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.dequeue())
print(q.dequeue())

print(q.is_empty())

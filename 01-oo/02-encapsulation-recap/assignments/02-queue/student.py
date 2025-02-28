class Queue:
    def __init__(self):
        self.__queue = []

    def add(self,item):
        self.__queue.append(item)

    def next(self):
        return self.__queue.pop(0)
    
    def is_empty(self):
        return len(self.__queue) == 0
    
queue= Queue()
queue.add("Alice")
queue.add("Bob")
queue.add("Charlie")
print(queue.next())
print(queue.next())
print(queue.next())
print(queue.is_empty())
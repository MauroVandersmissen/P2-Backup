class CircularBuffer:
    def __init__(self,max_size):
        self.max_size=max_size
        self.buffer=[]
        self.size=0

    def add(self,item):
        if self.size==self.max_size:
            self.buffer.pop(0)
            self.size-=1
        self.buffer.append(item)
        self.size+=1
    
    def __getitem__(self,index):
        if index>=self.size:
            raise IndexError
        return self.buffer[index]
    
    def __len__(self):
        return self.size
    
buffer=CircularBuffer(3)
print(len(buffer))
buffer.add("a")
buffer.add("b")
buffer.add("c")
print(len(buffer))
print(buffer[0])
print(buffer[1])
print(buffer[2])
buffer.add("d")
print(len(buffer))
print([buffer[0],buffer[1],buffer[2]])
buffer.add("e")
print(len(buffer))
print([buffer[0],buffer[1],buffer[2]])
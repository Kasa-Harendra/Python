class queue():
    def __init__(self,value=None):
        self.list = []
        if value is not None:
            self.value = value
            self.front = 0
            self.rare = 0
        else:
            self.front = -1
            self.rare = -1
        return
    
    def isempty(self):
        return self.front == self.rare
            
    def enqueue(self,value):
        self.rare+=1
        self.list.insert(value,self.rare)
        print(f'{value} pushed succesfully')
        return
        
    def dequeue(self):
        if self.isempty():
            print("Queue empty")
            return
        print(f'Deleted element: {self.list[self.front+1]}')
        self.front += 1
        return
    
    def display(self):
        if self.isempty():
            print("Queue is empty")
        else:
            print("Front element -->",end = ' ')
            for i in self.list[self.front+1:self.rare+1]:
                print(f'| {i} | ',end = '')
            print('<-- rare element',end = '')
    
    def peek(self):
        if self.isempty():
            print("Stack underflow")
            return
        print(f'Front element-->{self.list[self.front+1]}')
        print(f'Rare element-->{self.list[self.rare]}')
        return
class Stack():
    def __init__(self,value=None):
        self.list = []
        if value is not None:
            self.value = value
            self.top = 0
        else:
            self.top = -1
        return
    
    def isempty(self):
        return self.top == -1
    
    def push(self,value):
        self.top+=1
        self.list.append(value)
        print(f'{value} pushed succesfully')
        return
        
    def pop(self):
        if self.isempty():
            print("Stack underflow")
            return
        item = self.list.pop(self.top)
        self.top -= 1
        return item
    
    def display(self):
        if self.isempty():
            print("Stack underflow")
            return
        print(f'Top element-->{self.list[self.top]} ',end = '')
        for i in range(self.top-1,-1,-1):
            print(self.list[i],end = ' ')
        return
    
    def peek(self):
        if self.isempty():
            print("Stack underflow")
            return
        print(f'Top element-->{self.list[self.top]}')
        return
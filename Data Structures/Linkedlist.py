class Node:
    def __init__(self,v=None):
        self.value = v
        self.next = None
        return
    def isempty(self):
        if self.value == None:
            return True
        else:
            return False
    def append(self,v):
        if self.isempty():
            self.value = v
            return
        temp = self
        newnode = Node(v)
        while temp.next != None:
            temp = temp.next
        temp.next = newnode
        return
    def delete(self,x):
        if self.isempty():
            return
        if self.value == x:
            if self.next == None:
                self.value = None
                return
            else:
                self.value = self.next.value
                self.next = self.next.next
                return
        temp = self
        while temp.next != None:
            if temp.next.value == x:
                temp.next = temp.next.next
                return self
            else:
                temp = temp.next
        return
    def insert(self,v):
        if self.isempty():
            self.value = v
            return
        newnode = Node(v)
        (self.value,newnode.value) = (newnode.value,self.value)
        (self.next,newnode.next) = (newnode,self.next)
        return
    def display(self):
        selflist = []
        if self.isempty():
            return
        temp = self
        while temp!= None:
            selflist.append(temp.value)
            temp = temp.next
        return (str(selflist))
        
    

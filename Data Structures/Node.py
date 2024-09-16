class Node:
    def __init__(self,initval = None):
        self.value = initval
        self.next = None
        return
    def isempty(self):
        return(self.value==None)
    def insert(self,v):
        if self.isempty():
            self.value = v
            return
        new = Node(v)
        (self.value,new.value)=(new.value,self.value)
        (self.next,new.next)=(new,self.next)
        return
    def append(self,v):
        if self.isempty():
            self.value = v
            return
        new = Node(v)
        temp = self
        while temp.next!=None:
            temp = temp.next
        temp.next = new
        return
    def delete(self,v):
        if self.isempty():
            return
        if self.value == v:
            if self.next == None:
                self.value = None
            else:
                self.value = self.next.value
                self.next = self.next.next
                return
            temp = self
            while temp.next != None:
                if temp.next.value == v:
                    temp.next = temp.next.next
                    return self
                else:
                    temp = temp.next
            return

    def display(self):
        l = []
        temp = self
        while temp!=None:
            print(temp.value,end = " ")
            temp = temp.next

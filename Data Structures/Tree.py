class Tree:
    def __init__(self,v=None):
        self.value = v
        if self.value:
            self.left = Tree()
            self.right = Tree()
            return
        else:
            self.left = None
            self.right = None
            return
    def isempty(self):
        return(self.value == None)
    def inorder(self):
        if self.isempty():
            return []
        else:
            return(self.left.inorder()+[self.value]+self.right.inorder())
    def display(self):
        print(self.inorder())
    def find(self,v):
        if self.isempty():
            return
        if self.value == v:
            return True
        elif self.value > v:
            return self.left.find(v)
        elif self.value < v:
            return self.right.find(v)
        return False
    def insert(self,v):
        if self.isempty():
            self.value = v
            self.left = Tree()
            self.right = Tree()
            return
        if self.value>v:
            self.left.insert(v)
            return
        if self.value<v:
            self.right.insert(v)
            return
    def makeempty(self):
        self.value = None
        self.left = None
        self.right = None
        return
    def copyright(self):
        self.value = self.right.value
        self.left = self.right.left
        self.right = self.right.right
        return
    def minval(self):
        if self.isempty():
            return
        temp = self
        while temp.left!=None:
            temp = temp.left
        return temp.value
    def delete(self,v):
        if self.isempty():
            return
        if self.value > v:
            self.left.delete(v)
        if self.value>v:
            self.right.delete(v)
        if self.value == v:
            if self.isleaf():
                self.value = None
            elif self.left.isempty():
                self.copyright()
            else:
                self.value = self.left.maxval()
                self.left.delete(self.left.maxval())
            return
    def isleaf(self):
        return (self.left==None and self.right==None)
    def length(self):
        if self.value == None:
            return 0
        elif self.isleaf():
            return 1
        else:
            return (1+self.left.length()+self.right.length())

            
    

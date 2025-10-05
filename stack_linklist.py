class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
class Stack:
    def __init__(self):
        self.top = None

    def push(self,value):
        newNode = Node(value)
        newNode.next = self.top    
        self.top = newNode
            
    def pop(self):
        temp = self.top
        print("POP: ",temp.data)
        self.top = temp.next
        del temp

    def display(self):
        temp = self.top
        while(temp != None):
            print(temp.data,end="->")
            temp = temp.next
        print("None")        

s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.display()
s1.pop()
s1.display()
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class NodeLinking:
    def __init__(self):
        self.head = None
    def push(self,val):
        newNode = Node(val)
        if(self.head == None):
            self.head = newNode
        else:
            temp = self.head
            temp.next = newNode
            temp = newNode
    def display(self):
        temp = self.head
        while(temp):
            print(f"{temp.data}",end="->")
            print("None")
            temp = temp.next

l1 = NodeLinking()
l2 = NodeLinking()
l1.push(10)
l1.push(20)
l1.display()
l2.push(30)
l2.push(40)
l1.display()


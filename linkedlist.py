class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def pop(self):
        temp = self.head      
        print(f"POP: {self.head.data}")
        self.head = temp.next
        del temp

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data,end="->")
            temp = temp.next
        print("None")

l1 = LinkedList()
l1.push(10)
l1.push(20)
l1.push(30)
l1.push(40)
l1.display()
l1.pop()
l1.display()
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Queues:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value):
        newNode = Node(value)
        if (self.head == None):
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def pop(self):
        temp = self.head
        print("POP: ",temp.data)
        self.head = temp.next
        del temp

    def display(self):
        temp = self.head
        while(temp != None):
            print(temp.data,end="->")
            temp = temp.next    
        print("None")                
q1 = Queues()
q1.push(10)
q1.push(20)
q1.push(30)
q1.push(40)
q1.display()
q1.pop()
q1.display()
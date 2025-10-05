class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertHead(self, val):
        newNode = Node(val)
        if (self.head == None):
            self.head = self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def insertTail(self, val):
        newNode = Node(val)
        if (self.head == None):
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def insertIndex(self, val, idx):
        newNode = Node(val)
        pos = 2
        if (self.head == None):
            self.head = self.tail = newNode
        elif (idx == 1):
            newNode.next = self.head
            self.head = newNode
        else:
            temp = self.head
            while (self.head.next and pos != idx):
                temp = temp.next
                pos += 1
            newNode.next = temp.next
            temp.next = newNode

    def deleteHead(self):
        temp = self.head
        temp = temp.next
        del self.head
        self.head = temp

    def delateTail(self):
        temp = self.head
        while (temp.next and temp.next != self.tail):
            temp = temp.next
        del self.tail
        self.tail = temp

    # def deleteIndex(self, idx):
    #     temp = self.head
    #     pos = 2
    #     while (temp.next and pos != idx):


    def Display(self):
        temp = self.head
        while (temp):
            print(temp.data, end="--->")
            temp = temp.next
        print("None")


l1 = LinkedList()

l1.insertTail(10)
l1.insertTail(20)
l1.insertHead(30)
l1.insertTail(40)



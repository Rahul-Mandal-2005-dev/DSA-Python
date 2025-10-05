class Node:
    def __init__(self, val: int) -> None:
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insertHead(self, val: int) -> int:
        newNode: Node = Node(val)
        if (self.head == None):
            self.head = self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def insertTail(self, val: int) -> int:
        newNode: Node = Node(val)
        if (self.head == None):
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def insertIndex(self, val: int, idx: int) -> None:
        newNode = Node(val)
        pos = 2
        if (self.head == None):
            self.head = self.tail = newNode
        elif (idx == 1):
            newNode.next = self.head
            self.head = newNode
        else:
            temp: Node = self.head
            while (self.head.next and pos != idx):
                temp = temp.next
                pos += 1
            newNode.next = temp.next
            temp.next = newNode

    def deleteHead(self) -> None:
        temp: Node = self.head
        temp = temp.next
        del self.head
        self.head = temp

    def delateTail(self) -> None:
        temp: Node = self.head
        while (temp.next and temp.next != self.tail):
            temp = temp.next
        del self.tail
        self.tail = temp

    def deleteIndex(self, idx: int) -> None:
        temp: Node = self.head
        pos: int = 2
        if (idx == -1):
            self.head = temp.next
            del temp
        else:
            while (temp.next and pos != idx):
                temp: Node = temp.next
                pos += 1
            delNode = temp.next
            temp.next = temp.next.next
            del delNode


    def Display(self) -> None:
        temp: Node = self.head
        while (temp):
            print(temp.data, end="--->")
            temp = temp.next
        print("None")


l1 = LinkedList()

l1.insertTail(10)
l1.insertTail(20)
l1.insertTail(30)
l1.insertTail(40)


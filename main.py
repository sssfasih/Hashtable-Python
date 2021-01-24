class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def InsertatFirst(self, value):
        new_node = Node(value)
        x = self.head
        # to check if list is empty or not
        if x == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def InsertatEnd(self, value):
        new_node = Node(value)
        if (self.head == None):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def DeleteatFirst(self):
        if self.head == None:
            raise SystemError("Empty linked list")

        self.head = self.head.next

    def DeleteatEnd(self):
        if self.head == None:
            raise SystemError("Empty linked list")

        tempvar = self.head
        while tempvar.next != self.tail:
            tempvar = tempvar.next

        self.tail = tempvar
        self.tail.next = None

    def Head(self):
        return self.head.value

    def Tail(self):
        return self.tail.value

    def Print(self):
        a = self.head
        # traverse the linked list
        while a:
            print(a.value)
            a = a.next

'''
a = LinkedList()
a.InsertatFirst(232)
a.InsertatFirst(423)
a.InsertatFirst(213)
a.InsertatFirst(88)
a.InsertatEnd(99)
a.DeleteatFirst()
a.DeleteatEnd()
a.Print()
print("Head = ", a.head.value)
print("Tail = ", a.tail.value)
'''


class HashTable:
    def __init__(self, size):
        self.data = [None for i in range(size)]
        self.size = size

    def Insert(self, element, index):
        if index < 0 or index >= self.size:
            raise IndexError("Out of Index")

        if type(self.data[index]) != LinkedList:
            print("No Linked list")
            # Create a linked list at this place
            self.data[index] = LinkedList()
            # initialize node with value = "element"
            tempvar = Node(element)
            #Insert node into Linked list
            self.data[index].InsertatFirst(tempvar)

        else:
            print("Linked List exists")
            # initialize node with value = "element"
            tempvar = Node(element)
            # Insert node into Linked list
            self.data[index].InsertatFirst(tempvar)

    def ShowLinkedList(self,index):
        return self.data[index]



def Hash(something,tablesize):
    if type(something) == int:
        total = 0
        something = str(something)
        for calculation in something:
            total = total+int(calculation)
        return total % tablesize

HashTable = HashTable(10)

HashTable.Insert(489898,Hash(489898,10))

HashTable.Insert(8,0)
HashTable.Insert(777,1)

HashTable.Insert(5,0)

linklist =HashTable.ShowLinkedList(0).Print()

print(Hash(523,10))


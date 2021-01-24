class Node(object):

    def __init__(self, value):
        self.value = value
        self.Next_Node = None
        self.Previous_Node = None

    def __str__(self):
        return str(self.value)


class DoublyLinkedList:

    def __init__(self):

        self.Head = None
        self.Tail = None

    def InsertatFirst(self, value):

        head = self.Head
        new_node = Node(value)

        #if empty Linkedlist
        if head is None:
            self.Head = new_node
            self.Tail = new_node

        # If non-empty LinkedList
        else:
            new_node.Next_Node = head
            new_node.Previous_Node = None
            self.Head = new_node


    def InsertatEnd(self, value):
        head = self.Head
        new_node = Node(value)

        # if empty Linkedlist
        if head is None:
            self.Head = new_node
            self.Tail = new_node
            new_node.Previous_Node = None

        # if non-empty Linkedlist
        else:
            # Transverse till head.next exists.
            while head.Next_Node is not None:
                head = head.Next_Node
                # end while

            new_node.Previous_Node = head
            head.Next_Node = new_node
            self.Tail = new_node

    def Get_Head(self):

        return self.Head

    def Get_Tail(self):

        return self.Tail

    def Insert_After(self, existing_val, new_val):

        if self.Tail.value == existing_val:

            self.Insert_At_End(new_val)

        else:

            head = self.Head
            new_node = Node(new_val)

            # Transverse till head is not not None
            while head:

                # if head matches given value
                if head.value == existing_val:

                    # Add new_node after it
                    new_node.Next_Node = head.Next_Node
                    head.Next_Node = new_node
                    new_node.Previous_Node = head.Previous_Node
                    head.Previous_Node = new_node
                head = head.Next_Node

    def DeleteatFirst(self):

        head = self.Head
        if head is None:
            raise "List is empty"

        self.Head = head.Next_Node
        self.Head.Previous_Node = None

    def DeleteatEnd(self):

        head = self.Head
        if head is None:
            raise "List is empty."

        while head.Next_Node != self.Tail:
            head = head.Next_Node
        self.Tail = head
        self.Tail.Next_Node = None

    def Delete_By_Value(self, value):

        if self.Tail.value == value:
            self.DeleteAtEnd()
        elif self.Head.value == value:
            self.DeleteatFirst()
        else:
            x = self.Head
            while x.value != value:
                x = x.Next_Node
            x.value = x.Next_Node.value
            x.Next_Node = x.Next_Node.Next_Node

    def Print(self):
        x = self.Head

        itration = ""

        while x:
            itration += str(x.value) + " -> "
            x = x.Next_Node
        if x == None:
            itration += str(x)
        print(itration)



a = DoublyLinkedList()
a.InsertatFirst(232)
a.InsertatFirst(423)
a.InsertatFirst(213)
a.InsertatFirst(88)
a.InsertatEnd(99)
a.DeleteatFirst()
a.DeleteatEnd()
a.Print()
a.Print()
print("Head = ", a.Get_Head())
print("Tail = ", a.Get_Tail())


'''
Db = LinkedList()
Db.Insert_At_First(1)
Db.Insert_At_First(2)
Db.Insert_At_End(3)
Db.Insert_At_End(4)
Db.Insert_After(2, 10)
print(Db.Head_Tail())
Db.Print()
Db.Delete_At_First()
Db.Delete_At_End()
Db.Delete_By_Value(10)
Db.Print()
'''

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

'''
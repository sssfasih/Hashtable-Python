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

        # if empty Linkedlist
        if head is None:
            self.Head = new_node
            self.Tail = new_node

        # If non-empty LinkedList
        else:
            new_node.Next_Node = head
            new_node.Previous_Node = None
            self.Head.Previous_Node = new_node
            self.Head = new_node

    def Get_Head(self):

        return self.Head

    def Get_Tail(self):

        return self.Tail

    def DeleteatFirst(self):

        head = self.Head
        if head is None:
            raise IndexError("List is empty.")

        self.Head = head.Next_Node
        self.Head.Previous_Node = None

    def DeleteatEnd(self):

        pointer = self.Head
        if pointer is None:
            raise IndexError("List is empty.")

        # loop till pointer's next node is not tail
        while pointer.Next_Node != self.Tail:
            pointer = pointer.Next_Node

        self.Tail = pointer
        self.Tail.Next_Node = None


    def Print(self):
        x = self.Head

        itration = ""

        while x:
            itration += str(x.value) + " -> "
            x = x.Next_Node

        if itration == "":
            print("Empty Linked List")

        elif x == None:
            itration += 'null'
        print(itration)


'''
a = DoublyLinkedList()
a.InsertatFirst(232)
a.InsertatFirst(423)
a.InsertatFirst(213)
a.Delete_By_Value(423)
a.Insert_After(232, 10)
a.InsertatFirst(88)
a.InsertatEnd(99)
a.DeleteatFirst()
a.DeleteatEnd()
a.Print()
a.Print()
print("Head = ", a.Get_Head())
print("Tail = ", a.Get_Tail())
'''


class HashTable:
    def __init__(self, size):
        self.data = [None for i in range(size)]
        self.size = size

    def Insert(self, element):
        # Calculate Hash index
        index = self.__Hash(element)

        # Check Hash index
        if index < 0 or index >= self.size:
            raise IndexError("Out of Index")

        # If there is no linked List already at index
        if type(self.data[index]) is not DoublyLinkedList:
            # print("No Linked list")
            # Create a linked list at this place
            self.data[index] = DoublyLinkedList()
            # initialize node with value = "element"
            tempvar = Node(element)
            # Insert node into Linked list
            self.data[index].InsertatFirst(tempvar)

        # If there is linked list present at index
        else:
            # print("Linked List exists")
            # initialize node with value = "element"
            tempvar = Node(element)
            # Insert node into Linked list
            self.data[index].InsertatFirst(tempvar)

    def ShowLinkedList(self, index):

        linked_list = self.data[index]
        if not linked_list:
            linked_list = DoublyLinkedList()

        return linked_list

    def __Hash(self, element):
        total = 0

        # Hash Calculation if element is integer
        if type(element) == int:
            element = str(element)
            for calculation in element:
                total = total + int(calculation)


        # Hash Calculation if element is string
        elif type(element) == str:

            for calculation in element:
                total += ord(calculation)

        else:
            raise SystemError("Hash Function supports strings and integers only")

        tablesize = self.size
        return total % tablesize


HashTable = HashTable(10)

HashTable.Insert(489898)
HashTable.Insert(8)
HashTable.Insert(777)
HashTable.Insert(777)
HashTable.Insert(778)
HashTable.Insert("Pepsi")
HashTable.Insert("7up")
HashTable.Insert("Sprite")
HashTable.Insert("Marinda")
HashTable.Insert(124)
HashTable.Insert(14)
HashTable.Insert(23)
HashTable.Insert(29)
HashTable.Insert("Coke")
HashTable.Insert("Tea")
HashTable.Insert("Elephant")
HashTable.Insert("Zebra")
HashTable.Insert("lalalala")
HashTable.Insert(777)

HashTable.Insert(5)

HashTable.ShowLinkedList(1).Print()

'''for loop in range(100):

    HashTable.ShowLinkedList(loop).Print()'''
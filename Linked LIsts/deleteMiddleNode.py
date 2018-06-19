# We will be given only the node as data
# Delete node in between the first and the last node

# Defining the Node class
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

# Defining the linkedList
class linkedList:
    def __init__(self):
        self.tail = None
        self.head = None

    # Defining method to add data to the Linked List
    def append(self, data):
        node = Node(data)

        # If the List is not empty the we add data
        # in the head
        if self.head:
            self.head.next = node
            self.head = node
        # If the List is empty then we add data
        # in the tail
        else:
            self.tail = node
            self.head = self.tail
        return self.head

    # Defining the display() method to display the Linked List
    def display(self):
        current = self.tail
        while current:
            print(current.data, end = ' ')
            current = current.next
        print()

    # Defining deleteMiddleNode() method to delete the given node
    def deleteMiddleNode(self, node):
        if node.data == None or node.next == None:
            return False
        else:
            next = node.next
            node.data = next.data
            node.next = next.next


# Defining the main() function
def main():
    lst = linkedList()

    # Calling the append method to add data into the Linked List
    Ist = lst.append(10)
    IInd = lst.append(40)
    IIIrd = lst.append(20)
    IVth = lst.append(90)
    Vth = lst.append(60)

    # Calling the display() method to display the Linked List
    # before deleting any node in between the First and the Last node
    lst.display()

    # Calling the deleteMiddleNode() method to delete a node in between
    # the First and the Last node
    lst.deleteMiddleNode(IIIrd)

    # Calling the display() method again to display the Linked List after
    # deleting the a node in between the First and the Last node
    lst.display()

# Calling the main() function
if __name__ == '__main__':
    main()

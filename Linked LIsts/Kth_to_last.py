# It is an iterative solution
# Defining the Node
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

#Defining the Linked List class
class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Method to add data to the linked List
    def append(self, data):
        node = Node(data)

        # If the linked List is not empty then we add
        # data to the head of the List
        if self.head:
            self.head.next = node
            self.head = node
        # If the Linked List is empty we add data to the tail
        # of the list
        else:
            self.tail = node
            self.head = self.tail

    # Method to display() the Linked List
    def display(self):
        current = self.tail
        while current:
            print(current.data, end = ' ')
            current = current.next
        print()

    # Method to return the data Kth to the last
    def KthToLast(self, k):
        lst1 = self.tail
        lst2 = self.tail

        # Move the lst1 to the Kth Position from the beginning of the List
        for i in range(k):
            if lst1.data == None:
                print("Out of bound")
                return 0
            else:
                lst1 = lst1.next

        # Move the lst1 and lst2 until lst1 == None
        # Then the position of lst2 will be the Kth Node to the last
        while(lst1):
            lst1 = lst1.next
            lst2 = lst2.next

        print("Data in the {}th node to the last: {}".format(k, lst2.data))

# Defining the main() function
def main():
    lst = linkedList()

    # Calling the append() method to add data to the Linked List
    lst.append(2)
    lst.append(3)
    lst.append(89)
    lst.append(67)
    lst.append(90)
    lst.append(45)
    lst.append(10)

    # Calling the display() method to display the Linked List
    lst.display()

    # Calling the KthToLast() method to know the Kth node's data from the last
    lst.KthToLast(3)
    lst.KthToLast(7)


# Calling the main() function
if __name__ == "__main__":
    main()

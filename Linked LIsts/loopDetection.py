#!/usr/bin/python

# This program checks a loop in the Linked List and returns
# the node at the beginning of the loop
#
#
# Defining the class Node()
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
        # in the tail
        if self.tail:
            self.tail.next = node
            self.tail = node
        # If the List is empty then we add data
        # in the head
        else:
            self.head = node
            self.tail = self.head
        return self.head, self.tail

    # Defining the display() method to display the Linked List
    def display(self):
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.next
        print()

    # Defining a method make_loop() to make a loop in the List
    def make_loop(self, first_node, last_node):
        last_node.next = first_node

    # Defining a method return_node() to return the first node of the loop
    def return_node(self, start):
        slow = start
        fast = start
        while (fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow.data
        return False


# Defining the main() function
def main():
    lst = linkedList()

    # Calling the append() method to add data into the Linked List
    l1, l2 = lst.append(10)
    l1, l2 = lst.append(20)
    l1, l2 = lst.append(30)
    l1, l3 = lst.append(40)
    l1, l2 = lst.append(50)
    l1, l2 = lst.append(60)
    l1, l2 = lst.append(70)
    # Calling the display() method on the Linked List to display its contents
    lst.display()

    # Calling the make_loop() method to make a loop.
    lst.make_loop(l3, l2)

    # Calling the return_node() method to return the first node
    # of the Loop 
    result = lst.return_node(l1)

    if result == False:
        print("I doesn't contain any loop")
    else:
        print("It contains loop and the first node of the loop is {}".format(result))

# Calling the main() function
if __name__ == "__main__":
    main()

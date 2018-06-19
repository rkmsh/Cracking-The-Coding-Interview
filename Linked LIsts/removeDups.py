# Solution when no buffer is allowed
# Defining the Node

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next =None

# Defining the Linked List class
class linkedList:
    def __init__(self):
        self.tail = None
        self.head = None

    # Method to add data into the Linked List
    def append(self, data):
        node = Node(data)

        if self.head:                      # If the Linked List is not empty then
            self.head.next = node          # We add data in the head
            self.head = node
        else:                               # If the Linked List is empty then
           self.head = node                # We add data in the head and in the tail
           self.tail = node

    # Method to display the Linked List
    def display(self):
        current = self.tail
        while current:
            print(current.data, end = " ")
            current = current.next
        print()
        
    # Method to remove duplicates
    def removeDups(self):
        current = self.tail
        while current:
            runner = current
            while runner.next:
                if runner.next.data == current.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next


def main():
    lst = linkedList()
    lst.append(2)
    lst.append(3)
    lst.append(4)
    lst.append(2)
    lst.append(5)
    lst.append(5)
    lst.append(4)

    # Calling the display() method before removing duplicates
    lst.display()

    # Calling the removeDups() method to remove duplicates
    lst.removeDups()

    # Calling the display() method to display the Linked List after removing duplicates
    lst.display()


# Calling the main() function
if __name__ == "__main__":
    main()

# The following code will make a partition around a given number
# such that the numbers smaller than the given number will appear
# prior to the numbers greater or equal to the given number

# defining the Node Class
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

# defining the LinkedList class
class linkedList:
    def __init__(self):
        self.tail = None
        self.head = None

    # defining a method append() to add data into the Linked List
    def append(self, data):
        node = Node(data)

        #If the List is not empty then we add data to the head
        if self.head:
            self.head.next = node
            self.head = node
        #If the List is empty then we add data to the tail
        else:
            self.tail = node
            self.head = self.tail
        return self.tail

    # deefining a method display() to display data of the Linked List
    def display(self, current):
        while current:
            print(current.data, end = ' ')
            current = current.next
        print()

    # defining a method partition() to make partition around a given number
    def partition(self, List, num):
        # Initialising the before Linked List to store data smaller than
        # the given number
        beforeStart = None
        beforeEnd = None
        # Initialising the after Linked List to store data greater or equal
        # to the given number 
        afterStart = None
        afterEnd = None

        while List:
            next = List.next
            List.next = None
            # If the data is smaller then we add it to the before Linked List
            if List.data < num:
                if beforeEnd:
                    beforeEnd.next = List
                    beforeEnd = List
                else:
                    beforeStart = List
                    beforeEnd = beforeStart
            # If the data is greater or equal to the given number then we add
            # it to the after Linked List
            else:
                if afterEnd:
                    afterEnd.next = List
                    afterEnd = List
                else:
                    afterStart = List
                    afterEnd = afterStart
            List = next
        # Merging the two Linked Lists
        if beforeStart == None:
            return afterStart
        else:
            beforeEnd.next = afterStart
            return beforeStart

# Defining the main() function
def main():
    lst = linkedList()

    #Calling the append() method to add data into the Linked List
    fst = lst.append(70)
    fst = lst.append(10)
    fst = lst.append(60)
    fst = lst.append(40)
    fst = lst.append(100)
    fst = lst.append(80)

    # Calling the display() method to display the Linked List before making
    # partition
    lst.display(fst)

    # Calling the partition() method to make partition
    fst = lst.partition(fst, 70)

    # Calling the display() method again to display the Linked List after
    # making partition
    lst.display(fst)

# Calling the main() function
if __name__ == "__main__":
    main()

#!/usr/bin/python

# This program checks whether a given Linked List is
# Palindrome or Not
#
# First we will reverse the Linked List and compare it
# from the origiinal one
#
#
# Defining the Node() class
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

# Defining the linkedList() class
class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Defining a method append() to add data data into the Linked List
    def append(self, data):
        node = Node(data)

        # If the Linked List is not empty the we add data
        # into the tail of the Linked List
        if self.tail:
            self.tail.next = node
            self.tail = node
        # If the Linked LIst is empty then we add data into
        # the head of the Linked List
        else:
            self.head = node
            self.tail = self.head
        return self.head

    # Defining a method display() to display the contents of the Linked List
    def display(self, current):
        while current:
            print(current.data, end = ' ')
            current = current.next
        print()

    # Defining a method make_reverse() to reverse a Linked List
    def make_reverse(self, start):
        new_node = None
        while start:
            node = Node(start.data)
            node.next = new_node
            new_node = node
            start = start.next
        return new_node

    # Defining a method to check for palindrome
    def check_palindrome(self, list1, list2):
        if (list1 == None or list2 == None):
            return False
        while(list1 != None and list2 != None):
            if (list1.data != list2.data):
                return False
            list1 = list1.next
            list2 = list2.next
        return True


# Defining the main() function
def main():
    lst = linkedList()

    # Calling the append() method to add data into the Linked List
    l1 = lst.append(10)
    l1 = lst.append(20)
    l1 = lst.append(30)
    l1 = lst.append(20)
    l1 = lst.append(10)
    # Calling the display() method on the Original List to display
    # its contents
    lst.display(l1)

    # Calling the make_reverse() method to reverse the Linked List
    l2 = lst.make_reverse(l1)
    # Calling the display() method on the reversed List to
    # display its contents
    lst.display(l2)

    # calling the check_palindrome() method to check Palindrome
    if (lst.check_palindrome(l1, l2)):
        print("It is a Palindrome")
    else:   
        print("It is not a palindrome")


# Calling the main() function
if __name__ == "__main__":
     main()

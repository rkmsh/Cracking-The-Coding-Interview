#!/usr/bin/python

# This adds two numbers stored in different linked list and
# return the sum as a linked List
#
# They all will be in reverse order such that 1's digit is athe the head
# of the Linked List
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
        self.first_head = None
        self.first_tail = None
        self.sec_head = None
        self.sec_tail = None
        self.result_head = None
        self.result_tail = None

    # Defining a method append_1() to add data to the Fist Linked List
    def append_1(self, data):
        node = Node(data)

        # If the Linked List is not empty then we add data into the
        # tail of the Linked List
        if self.first_tail:
            self.first_tail.next = node
            self.first_tail = node
        # If the Linked List is empty the we add data to the head of
        # Linked List
        else:
            self.first_head = node
            self.first_tail = self.first_head
        return self.first_head

    # Defining a method append_2() to add data to Second Linked List
    def append_2(self,data):
        node = Node(data)

        # If the Linked List is not empty the we add data to the
        # tail of the Linked List
        if self.sec_tail:
            self.sec_tail.next = node
            self.sec_tail = node
        # If the Linked List is empty then we add data into
        # the head of the Linked List
        else:
            self.sec_head = node
            self.sec_tail = self.sec_head
        return self.sec_head

    # Defining a method append_r() to add data to the Result Linked List
    def append_r(self, data):
        node = Node(data)

        # If the Linked List is not empty then we add data to the
        # tail of the Linked List
        if self.result_tail:
            self.result_tail.next = node
            self.result_tail = node
        # If the Linked List is empty then we add data to the
        # head of the Linked List
        else:
            self.result_head = node
            self.result_tail = self.result_head
        return self.result_head

    # Defining a method display() to display the data of the Linked List
    def display(self, start):
        while start:
            print(start.data, end = ' ')
            start = start.next
        print()

    # Defining a method to add the two numbers and return the sum
    def sumList(self, list1, list2, carry = 0):
        if (list1 == None and list2 == None and carry == 0):
            return None
        value = carry
        if list1.data != None:
            value = value + list1.data
        if list2.data != None:
            value = value + list2.data
        result = value % 10
        self.append_r(result)
        if value >= 10:
            carry = 1
        else:
            carry = 0
        if (list1 != None or list2 != None):
            self.sumList(list1.next, list2.next, carry)

        return self.result_head

# Defining the main() function
def main():
    lst = linkedList()

    lst1 = lst.append_1(7)
    lst1 = lst.append_1(1)
    lst1 = lst.append_1(6)
    lst.display(lst1)

    lst2 = lst.append_2(5)
    lst2 = lst.append_2(9)
    lst2 = lst.append_2(2)
    lst.display(lst2)

    lstr = lst.sumList(lst1,lst2,0)
    lst.display(lstr)

if __name__ == "__main__":
    main()

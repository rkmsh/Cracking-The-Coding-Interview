#!/usr/bin/python

# This program add two numbers store in two different Linked List
# and return the sum as a Linked List
#
# In this case we have to add the numbers from backward and store the
# the result in backward direction int yhe Linked List
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

        # If the Linked List is not empty then we add data
        # before the head of the Linked List
        if self.result_head:
            node.next = self.result_head
            self.result_head = node
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

    # Defining a method know_len() to know the length of the Linked List
    def know_len(self, start):
        count = 0
        while start:
            count = count + 1
            start = start.next
        return count

    # Defining a method padding() to add 0  to the List which is
    # shorter in length
    def padding(self, len, start):
        for i in range(len):
            node = Node(0)
            node.next = start
            start = node
        return start

    # Defining a method to to add the Numbers and return the Sum
    def sum_List(self, list1, list2):
        if(list1 == None and list2 == None):
            return 0
        else:
            result = list1.data + list2.data + self.sum_List(list1.next, list2.next)
            val = result
            result = result % 10
            self.append_r(result)
            if val > 9:
                return 1
            else:
                return 0

    # Finishing the sum according to the last return
    def sumList(self, list1, list2):
        front = self.sum_List(list1,list2)
        if front == 1:
            self.append_r(1)
        return self.result_head

# Defining the main() function
def main():
    lst = linkedList()

    # calling the append_1() method to add data into the First Linked List
    l1 = lst.append_1(1)
    l1 = lst.append_1(2)
    l1 = lst.append_1(3)
    l1 = lst.append_1(4)
    # Calling the display() method on the First List to display its contents
    lst.display(l1)

    # calling the append_2() method to add data into the Second Linked List
    l2 = lst.append_2(5)
    l2 = lst.append_2(6)
    l2 = lst.append_2(7)
    # Calling the display() method on the Second List to display its contents
    lst.display(l2)

    len1 = lst.know_len(l1)
    len2 = lst.know_len(l2)
    if len1 < len2:
        # Calling the padding() method to add zero into the List of
        # shorter length before the head
        pd = lst.padding((len2-len1), l1)
        # Calling the sumList() method to add the two numbers and return the sum
        front = lst.sumList(l2, pd)
    elif len1 > len2:
        # Calling the padding() method to add zero into the List of
        # shorter length before the head
        pd = lst.padding((len1-len2), l2)
        # Calling the sumList() method to add the two numbers and return the sum
        front = lst.sumList(l1, pd)
    else:
        # Calling the sumList() method to add the two numbers and return the sum
        front = lst.sumList(l1, l2)


    # Calling the display() method to display the final result
    lst.display(front)

# Calling the main() function
if __name__ == "__main__":
    main()

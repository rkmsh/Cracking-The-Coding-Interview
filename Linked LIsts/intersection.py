#!/usr/bin/python

# This program chech if two given Linked List intersect
# or not
#
#
# Defining Node() class
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

    # Defining a method display() to display the data of the Linked List
    def display(self, start):
        while start:
            print(start.data, end = ' ')
            start = start.next
        print()

    # Defining a method count_node() to return the total number of nodes
    def count_node(self, start):
        count = 1
        while start.next:
            count = count + 1
            start = start.next
        return count, start.data

    # Defining a method move_node() to move next k node
    def move_node(self, k, start):
        while k > 0:
            start = start.next
            k = k - 1
        return start

    # Defining a method intersect() to make intersection between
    # two Linked Lists
    def intersect(self, large_l, k):
        self.sec_tail.next = self.move_node(k, large_l)
        while self.sec_tail:
            self.sec_tail = self.sec_tail.next

    # Defining a method collision() to check collision between the two Lists
    def collision(self, list1, list2):
        while(list1 != list2):
            list1 = list1.next
            list2 = list2.next
        if list1 == list2:
            print("They intersect at the node value {}".format(list1.data))
            return list1.data


# Defining the main() function
def main():
    lst = linkedList()

    # Calling the append_1() method to add data into the
    # First Linked List
    l1 = lst.append_1(10)
    l1 = lst.append_1(20)
    l1 = lst.append_1(30)
    l1 = lst.append_1(40)
    l1 = lst.append_1(50)
    l1 = lst.append_1(60)
    l1 = lst.append_1(70)
    # Calling the display() method on the Fisrt List
    # to display its contents
    lst.display(l1)

    # Calling the append_2() method to add data into the
    # Second Linked List
    l2 = lst.append_2(5)
    l2 = lst.append_2(15)
    l2 = lst.append_2(25)
    # Calling the intersect() method to make intersection
    # between the First and the Second Linked Lists
    lst.intersect(l1, 4)
    # Calling the display() method on the Second Linked List
    # to display its contents
    lst.display(l2)

    # Calling the count_node() method to know the last node and the total
    # number of nodes
    count1, node1 = lst.count_node(l1)
    count2, node2 = lst.count_node(l2)

    # If the value at last nodes of bothe Lists are not equal
    # then they are not intersecting
    if node1 != node2:
        print("They do not intersect")
        return 0

    # If First List has larger number of nodes
    if count1 > count2:
        # Calling the move_node() method to move the larger List
        # to ignore the initial nodes
        new_l1 = lst.move_node((count1-count2), l1)
        # Calling the collision() method to check the node at which
        # they intersect
        same_node = lst.collision(new_l1, l2)
        return 0
    # If Second List has larger number of nodes
    elif count1 < count2:
        # Calling the move_node() method to move the larger List
        # to ignore the initial nodes
        new_l2= lst.move_node((count2-count1), l2)
        # Calling the collision() method to check the node at which
        # they intersect
        same_node = lst.collision(l1, new_l2)
        return 0
    # If both Lists have equal number of nodes
    else:
        # Calling the collision() method to check the node at which
        # they intersect
        same_node = lst.collision(l1, l2)
        return 0


# Calling the main() function
if __name__ == "__main__":
    main()

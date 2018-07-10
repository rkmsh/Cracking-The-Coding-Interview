#!/usr/bin/python3
#
#
# This program always return the minnimum element in the stack
# Defining the class min_stack()
#
class min_stack:
    def __init__(self):
        self.stack = []
        self.stack_min = []
        self.tail = -1
        self.small = None
    # Defining a method push() to add data into the stack
    def push(self, data):
        self.stack.append(data)
        self.tail = self.tail + 1
        self.stack_min.append(data)
        self.min(self.stack_min)

    # Defining a method pop() to remove data from the stack
    def pop(self):
        value = self.stack[self.tail]
        del(self.stack[self.tail])
        self.tail = self.tail - 1
        del(self.stack_min[self.stack_min.index(value)])
        self.min(self.stack_min)

    # Defining a method min() to print the minnimum element in the stack
    def min(self, ls1):
        ls1.sort(reverse = True)
        try:
            if len(ls1) == 1:
                self.small = ls1[0]
            elif ls1[-1] < self.small:
                self.small = ls1[-1]
            print("Minnimum : {}".format(self.small))
        except IndexError:
            print("No Data")

# Defining the main() function
def main():
    # Creating an object of the class min_stack()
    ls2 = min_stack()

    # Calling the push() method to add data into the stack
    ls2.push(4)
    ls2.push(10)
    # Calling the pop() function to remove data from the stack
    ls2.pop()
    # Calling the push() method to add data into the stack
    ls2.push(2)
    # Calling the pop() function to remove data from the stack
    ls2.pop()
    ls2.pop()
    # Calling the push() method to add data into the stack
    ls2.push(5)
    ls2.push(3)

# Calling the main() function
if __name__ == "__main__":
    main()

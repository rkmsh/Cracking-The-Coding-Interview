#!/urs/bin/python3
#
#
# This program implements three stacks of into a single array
#
#
# Defining a class for the stacks
class stacks:
    def __init__(self, stackSize):
        self.array = [None] * stackSize * 3
        self.stackCapacity = stackSize
        self.first = -1
        self.sec = stackSize - 1
        self.third = stackSize * 2 - 1

    # Defining a method to add data into the stack
    def push(self, data, stackNo):
        if stackNo == 1:
            if self.first < self.stackCapacity - 1:
                self.first = self.first + 1
                self.array[self.first] = data
            else:
                print("First stack is full")
        elif stackNo == 2:
            if self.sec < self.stackCapacity * 2 - 1:
                self.sec = self.sec + 1
                self.array[self.sec] = data
            else:
                print("Second stack is full")
        elif stackNo == 3:
            if self.third < self.stackCapacity * 3 - 1:
                self.third = self.third + 1
                self.array[self.third] = data
            else:
                print("Third stack is full")
    # Defining a method to remove data from the respective stack
    def pop(self, stackNo):
        if stackNo == 1:
            if self.first == -1:
                print("First stack is empty")
            else:
                print("Poped Element from 1st stack is: {}".format(self.array[self.first]))
                self.first = self.first - 1
        elif stackNo == 2:
            if self.sec == self.stackCapacity - 1:
                print("Second stack is empty")
            else:
                print("Poped Element from the 2nd stack is: {}"
                      .format(self.array[self.sec]))
                self.sec = self.sec - 1
        elif stackNo == 3:
            if self.third == self.stackCapacity * 2 - 1:
                print("Third stack is empty")
            else:
                print("Poped Element from the 3rd stack is: {}"
                      .format(self.array[self.third]))
                self.third = self.third - 1
    # Defining a method to return the index value of
    # the last element of the respective stack
    def peek(self, stackNo):
        if stackNo == 1:
            print("Last element of 1st stack is at: {}".format(self.first))
        elif stackNo == 2:
            print("Last element of 2nd stack is at: {}".format(self.sec))
        elif stackNo == 3:
            print("Last element of 3rd stack is at: {}".format(self.third))

# Defining the main() function
def main():
    st = stacks(3)
    #Calling the push() method to add data
    st.push(3,1)
    st.push(5,2)
    st.push(8,3)
    st.push(10, 2)
    st.push(11, 2)
    st.push(12, 2)
    #Calling the pop() method to delete element from the respective stack
    st.pop(2)
    #Calling the peek method to to return the indes of the last element
    #of the respective stack
    st.peek(1)
    st.peek(2)
    st.peek(3)


# Calling the main() function
if __name__ == "__main__":
    main()

#!/usr/bin/python3

#Question Ninth of Arrays and Strings

#Method to check string_rotation
def string_rotation(first, sec):
    #If the length of first not equals second string
    #Then it does not satisfy the string_rotation condition
    if(len(first) != len(sec)):
        print("Do not satisfy the String Rotation.")
        return 0

    first = first + first
    if(sec in first):
        print("Satisfies the string Rotation")
    else:
        print("Do not satisfy the String Rotation.")


def main():
    #Ask the user to input the two required strings
    first = input("Enter the first string: ")
    sec = input("Enter the second string: ")

    #Call the string_rotation method
    string_rotation(first, sec)

if __name__ == "__main__":
    main()

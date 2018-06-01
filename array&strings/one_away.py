#!/usr/bin/python3

#Question fifth of arrays and strings

#Define a function to check the condition of replacement
def one_replace(first, sec):
    yes = False
    for i in range(len(first)):
        if(first[i] != sec[i]):
            if(yes):
                print("One_Replace is not satisfied")
                return 0
            yes = True
    print("One_Replace is satisfied.")
    return 0

#Define a function to check the condition of insertion
def insert(first, sec):
    yes  = False
    index1 = 0
    index2 = 0
    while(index1 < len(first) and index2 < len(sec)):
        if(first[index1] != sec[index2]):
            if(index1 != index2):
                print("One_Insertion is not satisfied.")
                return 0
            index2 = index2 + 2
        index1 = index1 + 1
        index2 = index2 + 1
    print("One_Insertion is satisfied.")
    return 0


#Take the strings from the user
first = input("Enter the first string: ")
sec = input("Enter the second string: ")

#If the length of first string equals second string
#Then we call one_replace() method to check for replacement
if(len(first) == len(sec)):
    one_replace(first, sec)
#If the length of the first string is less than second
#Then we call the insert() method to check for insertion
elif(len(first) + 1 == len(sec)):
    insert(first, sec)
#If the length of the second string is less than first
#Then we call the insert() method to check for insertion
elif(len(first) - 1 == len(sec)):
    insert(sec, first)
#If the above conditions are not satisfies by both the Strings
#Then we give a invalid message
else:
    print("Invalid Strings!!!!!!")

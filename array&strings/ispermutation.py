#Second question of arrays and strings
#To check if a string is permutation of the other

def main():
    first = input("Enter the first string: ") #Take the 1st string
    sec = input("Enter the second string: ") #Take the 2nd string

    first = ''.join(sorted(first)) #Sort the 1st string alphabetically

    sec = ''.join(sorted(sec)) #Sort the 2nd string alphabetically

    if(len(first) == len(sec)): #Check the length of the sorted strings
        print("Yes! the first string is permutation of the other") #If lenghts of both the strings are equal
    else:
        print("No! the first string is not permutation of the other ") #If lengths of both the strings are not equal


if __name__ == "__main__":
    main()

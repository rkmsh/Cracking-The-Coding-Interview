def main():
    #question one of first exercise
    #Get the string from the user
    ans = input("Enter the string: ")
    check = [] #Define a list
    n = 0
    for i in ans:
        if i in check:
            print("Duplicate!!!") #If the element already exist in the list print Duplicate
            n = 1
            break

        else:
            check.append(i) #If the element not in list then add the element to itself.

    if(n != 1):
        print("Do not contain Duplicates.")

if __name__ =="__main__":
    main()

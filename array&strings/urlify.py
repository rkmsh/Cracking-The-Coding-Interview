#!/usr/bin/python3

#Write a method to replace all the spaces
#with '%20'

#Take the string from the user
que  = input("Enter your string: ")
count = 0
for i in range(len(que)):
    if(que[i] == " "):
        count = count + 1    #Count total spaces

index = (len(que)+2*count)   #Total memory required to store the new string
new_array = [0]*index        #define a new array of the size index

for i in range(len(que)-1,-1,-1): #Loop to check the string in reverse order
    if(que[i]==" "):
        new_array[index-1]="0"
        new_array[index-2]="2"
        new_array[index-3]="%"
        index = index-3
    else:
        new_array[index-1] = que[i]
        index = index-1

new_array = ''.join(str(x) for x in new_array)
print("New string is: " + new_array)             #Print the new string

#!/usr/bin/python3

#Question fourth of arrays and strings

#Take input from the user
first = input("Enter the string: ")

first = first.replace(" ", "") #Remove all spaces from the string
#Sort the string alphabetically
first  = ''.join(sorted(first))

#Find that the total word count of the string is even or odd
#If it is even then there will be no alphabet of event Count
#If it is odd then there can be only one alphabet of even count
m = len(first)%2

arr = [0]*26 #An array to store alphabet count of the string

for i in range(len(first)):
    arr[ord(first[i])-97] = arr[ord(first[i])-97] + 1
count = 0
for i in range(26):
    if(arr[i]%2 == 1):
        count = count + 1    #Total no alphabets having odd count
if(m==1 and count==1):
    print("It is a permutation of palindrome.")
elif(m==0 and count==0):
    print("It is permutation of palindrome.")
else:
    print("It is not a permutation of palindrome.")

#!/usr/bin/python3

#Question sixth of Arrays and Strings

#Take the string from the user
bcomp = input("Enter your string: ")
count = 0
acomp = []
for i in range(len(bcomp)):
    count = count  + 1
    if(i+1 >= len(bcomp) or bcomp[i] != bcomp[i+1]):
        acomp.append(bcomp[i])
        acomp.append(count)
        count = 0
acomp = ''.join(str(x) for x in acomp)
print(acomp)

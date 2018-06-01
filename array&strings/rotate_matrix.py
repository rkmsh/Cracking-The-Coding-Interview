#!/usr/bin/python3

#Question seventh of Arrays and Stings
#Take the matrix n*n from the user
n = int(input("Enter the length of matrix: "))
print("Enter your matrix: ")
matrix = []
for i in range(n):
    matrix.append([])
    for j in range(n):
        matrix[i].append(int(input()))
print("Matrix before rotation: ")
print(matrix)

for layer in range(int(n/2)):
    first = layer
    last = n - 1 - layer
    for i in range(first, last):
        offset = i - first
        top = matrix[first][i]
        matrix[first][i] = matrix[last-offset][first]
        matrix[last-offset][first] = matrix[last][last - offset]
        matrix[last][last - offset] = matrix[i][last]
        matrix[i][last] = top

print("Matrix after rotation:")
print(matrix)

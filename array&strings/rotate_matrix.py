#!/usr/bin/python3

#Question seventh of Arrays and Stings
#Take the matrix n*n from the user
n = int(input("Enter the length of matrix: "))
print("Enter your matrix: ")
matrix = []
#Input matrix
for i in range(n):
    matrix.append([])
    for j in range(n):
        matrix[i].append(int(input()))
#Display the matrix before rotation
print("Matrix before rotation: ")
print(matrix)

for layer in range(int(n/2)):
    first = layer
    last = n - 1 - layer
    for i in range(first, last):
        offset = i - first
        #Store top->var:top
        top = matrix[first][i]
        #Move left->top
        matrix[first][i] = matrix[last-offset][first]
        #Move bottom->left
        matrix[last-offset][first] = matrix[last][last - offset]
        #Move right->bottom
        matrix[last][last - offset] = matrix[i][last]
        #Move var:top->right
        matrix[i][last] = top

#Display the matrix after rotation
print("Matrix after rotation:")
print(matrix)

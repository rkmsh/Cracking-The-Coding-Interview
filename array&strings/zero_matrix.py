#!/usr/bin/python3

#Question eighth of Arrays and Strings

#Method to make the whole row zero
def nullify_row(matrix, i, n):
    for j in range(n):
        matrix[i][j] = 0

#Method to make the whole column zero
def nullify_column(matrix, j, n):
    for i in range(n):
        matrix[i][j] = 0

def main():
    n = int(input("Enter the size of the matrix: "))
    matrix = []
    #Take the n*n matrix from the user
    for i in range(n):
        matrix.append([])
        for j in range(n):
            matrix[i].append(int(input()))

    print("Matrix before making rows and columns zero:")
    print(matrix)

    frow = False
    fcolumn = False

    #Check the first column for zero
    for i in range(n):
        if(matrix[i][0] == 0):
            fcolumn = True
            break

    #Check the first row for zero
    for j in range(n):
        if(matrix[0][j] == 0):
            frow = True
            break

    #Check the rest matrix for zero
    for i in range(1,n):
        for j in range(1,n):
            if(matrix[i][j] == 0):
                matrix[0][j] = 0
                matrix[i][0] = 0

    #Nullify the rows based on the zeroes in the first column
    for i in range(1, n):
        if(matrix[i][0] == 0):
            nullify_row(matrix, i, n)

    #Nullify the columns based on the zeroes in the first row
    for j in range(1, n):
        if(matrix[0][j] == 0):
            nullify_column(matrix, j, n)

    #If the First_row contain any zeroes
    #Make the whole row to zero
    if(frow):
        nullify_row(matrix,0,n)

    #If the First_column contain any zeroes
    #Make the whole column to zero
    if(fcolumn):
        nullify_column(matrix,0,n)

    print("Matrix after making rows and columns zero:")
    print(matrix)

if __name__ == "__main__":
    main()

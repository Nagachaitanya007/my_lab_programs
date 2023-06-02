# Take input for matrix dimensions
rows1 = int(input("Enter the number of rows for the first matrix: "))
cols1 = int(input("Enter the number of columns for the first matrix: "))
rows2 = int(input("Enter the number of rows for the second matrix: "))
cols2 = int(input("Enter the number of columns for the second matrix: "))

# Check if matrix multiplication is possible
if cols1 != rows2:
    print("Matrix multiplication is not possible. Number of columns in the first matrix must be equal to the number of rows in the second matrix.")
else:
    # Initialize matrices
    matrix1 = []
    matrix2 = []
    result_matrix = []

    # Take input for the first matrix
    print("Enter elements of the first matrix:")
    for i in range(rows1):
        row = []
        for j in range(cols1):
            element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
            row.append(element)
        matrix1.append(row)

    # Take input for the second matrix
    print("Enter elements of the second matrix:")
    for i in range(rows2):
        row = []
        for j in range(cols2):
            element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
            row.append(element)
        matrix2.append(row)

    # Perform matrix multiplication
    for i in range(rows1):
        row = []
        for j in range(cols2):
            element = 0
            for k in range(cols1):
                element += matrix1[i][k] * matrix2[k][j]
            row.append(element)
        result_matrix.append(row)

    # Print the result matrix
    print("Resultant matrix after multiplication:")
    for row in result_matrix:
        print(row)

def matrix_multiply(matrix_a, matrix_b):
    # Get dimensions of the matrices
    rows_a, cols_a = len(matrix_a), len(matrix_a[0])
    rows_b, cols_b = len(matrix_b), len(matrix_b[0])
     
    # Check if multiplication is possible
    if cols_a != rows_b:
        raise ValueError("Number of columns in matrix A must equal number of rows in matrix B.")
    
    # Initialize the result matrix with zeros
    result = [[0 for x in range(cols_b)] for x in range(rows_a)]
    
    # Perform matrix multiplication
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    
    return result

# Example usage
if __name__ == "__main__":
    matrix_a = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    matrix_b = [
        [7, 8],
        [9, 10],
        [11, 12]
    ]
    
    result = matrix_multiply(matrix_a, matrix_b)
    print("Resultant Matrix:")
    for row in result:
        print(row)
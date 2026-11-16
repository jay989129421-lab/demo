"""Assignment 4: Create arrays (matrices) and add two matrices.
Part A uses NumPy, Part B uses plain nested lists."""

import numpy as np

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("\nEnter elements of Matrix A:")
A = np.array([[int(input(f"A[{i}][{j}]: ")) for j in range(cols)] for i in range(rows)])

print("\nEnter elements of Matrix B:")
B = np.array([[int(input(f"B[{i}][{j}]: ")) for j in range(cols)] for i in range(rows)])

print("\nMatrix A:\n", A)
print("\nMatrix B:\n", B)

# Part A: using NumPy
print("\nA + B (NumPy):\n", A + B)

# Part B: using loops (without NumPy)
result = [[0] * cols for _ in range(rows)]
for i in range(rows):
    for j in range(cols):
        result[i][j] = int(A[i][j] + B[i][j])
print("\nA + B (using loops):")
for row in result:
    print(row)

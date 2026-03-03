import numpy as np
print("Enter elements for 5x3 matrix:")
A = []
for i in range(5):
    row = list(map(int, input().split()))
    A.append(row)
A = np.array(A)
print("Enter elements for 3x2 matrix:")
B = []
for i in range(3):
    row = list(map(int, input().split()))
    B.append(row)
B = np.array(B)
product = np.dot(A, B)
print("Product Matrix (5x2):")
print(product)
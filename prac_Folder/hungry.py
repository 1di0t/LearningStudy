import numpy as np

# A = np.array([[1, 2], [3, 4]])

# locateInA = A[0,1]
# print(locateInA)


B = np.array([[1, 2, 3, 4, 5],
[ 6,  7,  8,  9, 10,],
[11, 12, 13, 14, 15],
[16, 17, 18, 19, 20],
[21, 22, 23, 24, 25]])

for row in B:
    print(row)

flattenB = B.flatten()
print(flattenB)

print(B[np.array([2,4]), np.array([0,2])])

import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(a)

a_mul = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

print(a_mul)

a1 = np.array([1, 2, 3])
a2 = np.array([[1],
               [2]])
print(a1 + a2)

a = np.array([[1, 2, 3],
              [2, 3, 4]])
print(a.T)

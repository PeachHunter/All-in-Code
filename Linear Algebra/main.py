from linalg.Matrix import Matrix

a = Matrix([[1, 2, 3], [0, 5, 6], [0, 0, 9]])
b = Matrix([[1, 2], [3, 4]])
c = Matrix([[1, 0], [0, 1]])
print(a.swap_col(1, 2))
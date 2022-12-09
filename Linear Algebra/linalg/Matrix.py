from typing import Union


class Matrix(object):
    def __init__(self, data):
        if isinstance(data, list):
            cols = [len(row) for row in data]
            if len(set(cols)) == 1:
                self.data = data
            else:
                raise ValueError("Invalid Input")
        else:
            raise TypeError("Data should be in the type of list")

    @property
    def row(self):
        """
        Get the number of rows of the matrix
        :return: int
        """
        return len(self.data)

    @property
    def col(self):
        """
        Get the number of columns of the matrix
        :return: int
        """
        return len(self.data[0])

    @property
    def transpose(self):
        """
        Transpose the matrix
        :return:
        """
        result = []
        for i in range(self.col):
            transposed_row = [row[i] for row in self.data]
            result.append(transposed_row)
        return Matrix(result)

    def __getitem__(self, key):
        """
        Return the data stored in the matrix
        :param key: the index
        :return: Matrix[i][j]
        """
        return self.data[key]

    def __str__(self):
        """
        Print the matrix
        :return: str
        """
        result = ""
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                result += str(self.data[i][j]) + " "
            result += "\n"
        return result

    def __add__(self, other):
        """
        Matrix Addition
        :param other: Matrix
        :return:
        """
        result = []
        if isinstance(other, Matrix):
            if other.row == self.row and other.col == self.col:
                for i in range(len(self.data)):
                    _result = []
                    for j in range(len(self.data[0])):
                        _result.append(self.data[i][j] + other.data[i][j])
                    result.append(_result)
            else:
                raise ValueError("Invalid Shape for Matrix Addition")
        elif isinstance(other, (int, float)):
            for i in range(len(self.data)):
                _result = []
                for j in range(len(self.data[0])):
                    _result.append(self.data[i][j] + other)
                result.append(_result)
        else:
            raise ValueError("Invalid Operand for Matrix Addition")
        return Matrix(result)

    def __sub__(self, other):
        """
        Matrix Subtraction
        :param other:
        :return:
        """
        result = []
        if isinstance(other, Matrix):
            if other.row == self.row and other.col == self.col:
                for i in range(len(self.data)):
                    _result = []
                    for j in range(len(self.data[0])):
                        _result.append(self.data[i][j] - other.data[i][j])
                    result.append(_result)
            else:
                raise ValueError("Invalid Shape for Matrix Addition")
        elif isinstance(other, (int, float)):
            for i in range(len(self.data)):
                _result = []
                for j in range(len(self.data[0])):
                    _result.append(self.data[i][j] - other)
                result.append(_result)
        else:
            raise ValueError("Invalid Operand for Matrix Addition")
        return Matrix(result)

    def __mul__(self, other):
        """
        Hadamard Multiplication for Matrices
        :param other:
        :return:
        """
        result = []
        if isinstance(other, Matrix):
            if other.row == self.row and other.col == self.col:
                for i in range(len(self.data)):
                    _result = []
                    for j in range(len(self.data[0])):
                        _result.append(self.data[i][j] * other.data[i][j])
                    result.append(_result)
            else:
                raise ValueError("Invalid Shape for Matrix Addition")
        elif isinstance(other, (int, float)):
            for i in range(len(self.data)):
                _result = []
                for j in range(len(self.data[0])):
                    _result.append(self.data[i][j] * other)
                result.append(_result)
        else:
            raise ValueError("Invalid Operand for Matrix Addition")
        return Matrix(result)

    def __eq__(self, other):
        """
        Matrix Comparison
        :param other:
        :return:
        """
        if not isinstance(other, Matrix):
            raise TypeError("Invalid Type of Input")
        else:
            if self.row == other.row and self.col == other.col:
                for i in range(self.row):
                    for j in range(self.col):
                        if self.data[i][j] != other.data[i][j]:
                            return False
            else:
                raise ValueError("Invalid Dimension")
        return True

    def __ne__(self, other):
        """
        Matrix Comparison
        :param other:
        :return:
        """
        return not self.__eq__(other)

    def __lt__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Invalid Type of Input")
        else:
            if self.row == other.row and self.col == other.col:
                for i in range(self.row):
                    for j in range(self.col):
                        if self.data[i][j] >= other.data[i][j]:
                            return False
            else:
                raise ValueError("Invalid Dimension")
        return True

    def __gt__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Invalid Type of Input")
        else:
            if self.row == other.row and self.col == other.col:
                for i in range(self.row):
                    for j in range(self.col):
                        if self.data[i][j] <= other.data[i][j]:
                            return False
            else:
                raise ValueError("Invalid Dimension")
        return True

    def __le__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Invalid Type of Input")
        else:
            if self.row == other.row and self.col == other.col:
                for i in range(self.row):
                    for j in range(self.col):
                        if self.data[i][j] > other.data[i][j]:
                            return False
            else:
                raise ValueError("Invalid Dimension")
        return True

    def __ge__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Invalid Type of Input")
        else:
            if self.row == other.row and self.col == other.col:
                for i in range(self.row):
                    for j in range(self.col):
                        if self.data[i][j] < other.data[i][j]:
                            return False
            else:
                raise ValueError("Invalid Dimension")
        return True

    def matmul(self, other):
        """
        Matrix Multiplication
        :param other:
        :return:
        """
        if isinstance(other, Matrix):
            if self.col == other.row:
                result = []
                for i in range(self.row):
                    _result = []
                    for j in range(other.col):
                        _result.append(sum([a * b for a, b in zip(self.data[i], other.transpose.data[j])]))
                    result.append(_result)
            else:
                raise ValueError("Invalid Input Size")

        else:
            raise ValueError("Invalid Input Type")
        return Matrix(result)

    def __matmul__(self, other):
        """
        Matrix Multiplication
        :param other:
        :return:
        """
        return self.matmul(other)

    def __len__(self):
        """
        return the size of the matrix
        :return:
        """
        return self.row * self.col

    def __iter__(self):
        self.current_row = 0
        return self

    def __next__(self):
        if self.current_row >= self.row:
            raise StopIteration
        else:
            result = self.data[self.current_row]
            self.current_row += 1
            return result

    def is_symmetric(self):
        """
        Whether the matrix is symmetric or not
        :return:
        """
        if self.row != self.col:
            return False
        return self == self.transpose

    def is_square(self):
        return self.col == self.row

    def is_diagonal(self):
        if not self.is_square():
            return False
        for i in range(self.row):
            for j in range(self.col):
                if i != j:
                    if self.data[i][j] != 0:
                        return False
        return True

    def is_upper_triangular(self):
        if not self.is_square():
            return False
        for i in range(self.row):
            for j in range(self.col):
                if i > j:
                    if self.data[i][j] != 0:
                        return False
        return True

    def is_lower_triangular(self):
        if not self.is_square():
            return False
        for i in range(self.row):
            for j in range(self.col):
                if i < j:
                    if self.data[i][j] != 0:
                        return False
        return True

    def det(self):
        """
        Use Recursion to Realize Determinant Calculation
        :return: value
        """
        if not self.is_square():
            raise ValueError("Non-square Matrix do not have determinant. Calculate Singular Value Instead!")
        if self.col == 1 and self.row == 1:
            return self.data[0][0]
        else:
            determinant = 0
            for j in range(self.col):
                multiplier = self.data[0][j]
                submatrix_data = []
                for i in range(1, self.row):
                    _submatrix_data = []
                    for k in range(self.col):
                        if k != j:
                            _submatrix_data.append(self.data[i][k])
                    submatrix_data.append(_submatrix_data)
                determinant += (-1) ** j * multiplier * Matrix(submatrix_data).det()
        return determinant

    def delete(self, *args, axis=0):
        """
        delete the row or col of a Matrix and return the result
        Note: This action will not modify the original data of the Matrix
        :param args: ids of row or col to delete
        :param axis: direction of the action
        """
        if axis == 0:
            if max(args) >= self.row:
                raise TypeError("Invalid Indices")
            elif len(set(args)) == self.row:
                raise TypeError("Null Matrix")
        if axis == 1:
            if max(args) >= self.col:
                raise TypeError("Invalid Indices")
            elif len(set(args)) == self.col:
                raise TypeError("Null Matrix")

        result = self.data.copy()
        if axis == 0:
            return Matrix([self.data[i] for i in range(self.row) if i not in args])
        if axis == 1:
            return Matrix([self.transpose.data[i] for i in range(self.col) if i not in args]).transpose

    def inv(self):
        """
        Calculate the inverse matrix
        :rtype: Matrix
        """
        if not self.is_square():
            raise TypeError("Invalid Input Shape!")
        inverse_res = [[0 for _ in range(self.col)] for _ in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                inverse_res[j][i] = (-1) ** (i + j) * self.delete(i, axis=0).delete(j, axis=1).det() / self.det()
        return Matrix(inverse_res)

    def swap_row(self, i, j):
        """
        swap two rows of the matrix
        :return:
        """
        if max(i, j) >= self.row or min(i, j) < 0:
            raise TypeError("Invalid Input!")
        result = self.data.copy()
        result[i], result[j] = result[j], result[i]
        return Matrix(result)

    def swap_col(self, i, j):
        """
        swap two cols of the matrix
        :param i:
        :param j:
        :return:
        """
        if max(i, j) >= self.col or min(i, j) < 0:
            raise TypeError("Invalid Input!")
        result = self.transpose.data.copy()
        result[i], result[j] = result[j], result[i]
        return Matrix(result).transpose

    def scalar_row(self, i, j, times):
        """
        Add or Subtract the i-th row from the times of j-th row
        :param i:
        :param j:
        :param times:
        :return:
        """


    # def gaussian_elim(self):
    #     result = self.data.copy()
    #     if self.row == 1:
    #         return Matrix(result)
    #     for i in range(1, self.row):
    #         for j in range(i):
    #             if result[i][j] != 0:
    #                 multiplier = result[i][j] / result[j][j]





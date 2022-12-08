from typing import Union
from linalg.Matrix import Matrix


class Vector(Matrix):

    def __init__(self, data):
        """
        Initiate a vector
        :param data:
        """
        if isinstance(data, list):
            if len(data[0]) == 1:
                super().__init__(data)
            else:
                raise ValueError("Invalid Vector shape")
        else:
            raise ValueError("Invalid Type")



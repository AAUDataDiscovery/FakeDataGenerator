import numpy as np


class Column:
    name: str
    column_dtype: np.dtype | None = None

    def __init__(self, name):
        self.name = name
        self.column_dtype = None

    def generate(self, rows):
        raise NotImplemented

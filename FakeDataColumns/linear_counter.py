import numpy as np
from .data_column import Column


class LinearColumn(Column):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.column_dtype = None

    def generate(self, rows):
        x = 0
        while True:
            yield np.arange(x, x+rows)
            x += rows

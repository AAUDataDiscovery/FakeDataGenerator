import numpy as np
import faker
from .data_column import Column


class RandomWord(Column):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.column_dtype = np.dtype("U10")
        self.faker_instance = faker.Faker()

    def generate(self, rows):
        while True:
            yield np.fromiter(self._generate_row(), self.column_dtype, count=rows)

    def _generate_row(self):
        while True:
            yield self.faker_instance.word()

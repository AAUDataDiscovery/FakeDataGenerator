import uuid

import numpy as np
from .fakedataindex import FakeDataIndex


class UUIDIndex(FakeDataIndex):
    def __init__(self):
        self.dtype = "U20"

    def generate(self, rows):
        """
        Args:
            rows: The amount of rows to generate

        Returns: a series that can be used for an index
        """
        x = 0
        while True:
            yield np.fromiter(self._generate_row(), dtype=self.dtype, count=rows)
            x += rows

    def _generate_row(self):
        while True:
            yield str(uuid.uuid4())

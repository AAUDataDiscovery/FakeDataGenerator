import math
import random
import numpy as np

from FakeDataColumns.data_column import Column


class SinWave(Column):
    def __init__(self, name: str, variance:int = 0, phase_variance: int = 0, noise: int = 0):
        super().__init__(name)
        self.column_dtype = None
        self.variance = random.randint(-variance, variance)
        self.phase_variance = phase_variance
        self.noise = noise

    def generate(self, rows):
        """Generate a sin wave based on the given variance and noise

        If there's no noise we can avoid the extra calculation
        Returns: a number in a series
        """
        # yield np.fromiter(self._generate_row(), dtype=self.column_dtype, count=rows)

        x = 0 + random.randint(-self.phase_variance, self.phase_variance)

        if self.noise:
            while True:
                yield np.fromiter(self._generate_with_noise(x), dtype=self.column_dtype, count=rows)
                # yield math.sin(x) + random.randint(-self.noise, self.noise)
                x += rows

        while True:
            yield np.fromiter(self._generate_without_noise(x), dtype=self.column_dtype, count=rows)
            # yield math.sin(x)
            x += rows

    def _generate_with_noise(self, x):
        while True:
            yield math.sin(x) + random.randint(-self.noise, self.noise) + self.variance
            x += 1

    def _generate_without_noise(self, x):
        while True:
            yield math.sin(x) + self.variance
            x += 1

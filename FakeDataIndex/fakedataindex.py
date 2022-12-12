import pandas as pd


class FakeDataIndex:
    def generate(self, rows):
        """
        Args:
            rows: The amount of rows to generate

        Returns: a series that can be used for an index
        """
        x = 0
        while True:
            yield pd.RangeIndex(x, x + rows)
            x += rows

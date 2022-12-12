from typing import Iterator

import pandas as pd

from FakeDataColumns import Column
from FakeDataIndex import FakeDataIndex


class DataGenerator:
    def __init__(self, *columns: Column, index: FakeDataIndex | None = None, chunk_size: int = 100000):
        """Initialise the columns and index for the generator
        Args:
            *columns: The columns that will be generated
            index: The type of index to build the dataframe with, defaults to a range index
        """
        if index is None:
            self.index = FakeDataIndex().generate(chunk_size)
        else:
            self.index = index.generate(chunk_size)
        self.columns = {column.name: column.generate(chunk_size) for column in columns}
        self.chunk_size = chunk_size

    def generate_rows(self, rows) -> Iterator[pd.DataFrame]:
        """Generate rows based on the defined columns

        Args:
            rows: The amount of rows to generate at a time

        Returns: A generator that provides the amount of rows specified
        """
        while True:
            yield pd.DataFrame(
                {name: next(gen) for name, gen in self.columns.items()},
                index=next(self.index)
            )

    def generate_csv(self, rows: int, file_path: str = "output.csv"):
        """Create a CSV with the given amount of rows
        The amount of data generated and written at a time depends on the chunk size specified

        Args:
            rows: The amount of rows to write
            file_path: The path to the file that needs to be written

        Returns: None
        """
        chunk_generator = self.generate_rows(min(self.chunk_size, rows))
        next(chunk_generator).to_csv(file_path, mode="w")
        current_row = self.chunk_size
        while current_row < rows:
            next(chunk_generator).to_csv(file_path, mode="a", header=False)
            current_row += self.chunk_size


if __name__ == "__main__":
    from FakeDataColumns import LinearColumn
    from FakeDataColumns import SinWave
    from FakeDataColumns import RandomWord
    from FakeDataIndex import DatetimeIndex

    col1 = LinearColumn(name="col1")
    col2 = SinWave(name="col2")
    col3 = RandomWord(name="col3")
    generator = DataGenerator(col1, col2, col3, index=DatetimeIndex(frequency="D"), chunk_size=10)
    generator.generate_csv(100)

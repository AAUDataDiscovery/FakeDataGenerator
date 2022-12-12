import uuid

import numpy as np
import pandas as pd

from .fakedataindex import FakeDataIndex


class DatetimeIndex(FakeDataIndex):
    def __init__(self, start="2016-01-01", frequency: str = "H"):
        self.start = pd.to_datetime(start)
        self.frequency = frequency
        self.dtype = "U20"

    def generate(self, rows):
        """
        Args:
            rows: The amount of rows to generate

        Returns: a series that can be used for an index
        """
        current_date = self.start
        while True:
            yield pd.period_range(current_date, freq=self.frequency, periods=rows)
            current_date += pd.Timedelta(rows,self.frequency)

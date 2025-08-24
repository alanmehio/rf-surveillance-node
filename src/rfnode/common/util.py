import json

import numpy as np


class Util:

    def __init__(self):
        pass

    @classmethod
    def generate_array(
        cls, freq_start: int, freq_end: int, freq_step: int, device_amount: int
    ) -> list[np.int64]:
        """
    
        Generates an array of frequencies based on the provided start, end, and step values.
        Args:
            freq_start (int): The starting frequencies in HZ.
            freq_end (int): The ending frequencies in HZ.
            freq_step (int): The step size for frequency increments in HZ.
            device_amount (int): The number of devices to split the frequencies into
.
        """
        frequencies = np.arange(freq_start, freq_end, freq_step, np.int64)
        return np.array_split(frequencies, device_amount)  # split of equal or near-equal size


class NumpyComplexEncoder(json.JSONEncoder):

    def default(self, obj) -> any:

        if isinstance(obj, complex):
            return (obj.real, obj.imag)
        else:
            return None


if __name__ == "__main__":
    arrs = Util.generate_array(1, 500, 10, 2)
    print(len(arrs))
    print(len(arrs[0]))
    print(len(arrs[1]))
    for arr in arrs:
        for i in arr:
            print(i)

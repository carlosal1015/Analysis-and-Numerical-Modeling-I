#!/usr/bin/env python

from tabulate import tabulate
import numpy as np
import pandas as pd

n = np.arange(start=1, stop=1e1)
a_n = np.array((2 * n - 1) / n)
b_n = np.array(1 / np.power(n, 3))
df = pd.DataFrame({"a_n": a_n, "b_n": b_n})
df.index += 1  # https://stackoverflow.com/a/20168416

print(tabulate(df, headers="keys"))

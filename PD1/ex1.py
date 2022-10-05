#!/usr/bin/env python

from tabulate import tabulate
import numpy as np
import pandas as pd

n = np.arange(start=1, stop=1e2)
# n = np.arange(start=1, stop=100)  # FIXME: para b(64)=0.428571
a_n = np.array((n + 3) / (n + 7))
b_n = np.array((np.power(2, n) + 3) / (np.power(2, n) + 7))
df = pd.DataFrame({"a_n": a_n, "b_n": b_n})
df.index += 1  # https://stackoverflow.com/a/20168416
# pd.set_option("display.precision", 12)
# print(df)
print(tabulate(df, headers="keys", floatfmt=".12f"))

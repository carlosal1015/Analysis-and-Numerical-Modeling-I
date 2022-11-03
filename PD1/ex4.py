#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tabulate import tabulate
import numpy as np
import pandas as pd

n = np.arange(start=1, stop=1e4)
a_n = np.array((n + 1) / (n - 2))
df = pd.DataFrame({"a_n": a_n})
df.index += 1  # https://stackoverflow.com/a/20168416

print(tabulate(df, headers="keys"))

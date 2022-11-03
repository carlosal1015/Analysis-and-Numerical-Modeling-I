#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tabulate import tabulate
import numpy as np
import pandas as pd

n = np.arange(start=1, stop=10)
alpha_n = np.array((n + 1) / n**2)
beta_n = np.array((n + 3) / n**3)
df = pd.DataFrame({"alpha": alpha_n, "beta": beta_n})
df.index += 1

print(tabulate(df, headers="keys"))

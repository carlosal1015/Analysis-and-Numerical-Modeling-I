#!/usr/bin/env python

import numpy as np
import pandas as pd

# from prettytable import PrettyTable

# x = PrettyTable()

# x.field_names = ["n", "$\hat{p}$ calculada", "p_{n} corregida", "Error relativo"]
# x.add_row(["0", 1295, 1158259, 600.5])
# x.add_row(["1", 5905, 1857594, 1146.4])

# print(x)

alfa_n = lambda n: n + 1 / n**2
beta_n = lambda n: n + 1 / n**3
# for i in range(1, 10 + 1):
#     print(i, alfa_n(i), beta_n(i))

x = np.random.randn(5)
y = np.sin(x)
df = pd.DataFrame({"x": x, "y": y})
df.plot("x", "y", kind="scatter")

#!/usr/bin/env python

# Alumnos
# Cristhian Caleb Blas Huaroc
# Carlos Alonso Aznarán Laos

## By default we use tabulate, if available
## However, tabulate is not available on all systems
## and therefore a fallback immplementation is also provided

# n represents sequence domain from one to ten

try:
    from tabulate import tabulate
    from numpy import arange, array, sin
    from pandas import DataFrame

    n = arange(start=1, stop=1e1 + 1)
    sequence = array(sin(1 / n) / (1 / n))
    table = DataFrame({"n * sin(1/n)": sequence})
    table.index += 1  # rows will start in one
    print(tabulate(tabular_data=table, headers="keys", floatfmt=".10f"))
except ModuleNotFoundError:
    ## Fallback implementation if tabulate was not found
    from math import sin

    n = [i for i in range(1, 10 + 1, 1)]
    sequence = [i * sin(1 / i) for i in n]
    print("n\tn * sin(1/n)")
    print("--\t---------------")
    for i, row in enumerate(sequence):
        print(f"{i + 1}\t{row:.10f}")

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from numpy.linalg import cond


a = np.array([[1, 2, 4], [4, 4, 1], [2, 3, 4]])
print("Tomando la norma frobenius : ", cond(a, "fro"))

print("Tomando la norma infinito : ", cond(a, np.inf))

print("Tomando la norma 1 : ", cond(a, 1))

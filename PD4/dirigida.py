#!/usr/bin/env python


# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


x = np.arange(start=1, stop=5, dtype=np.float64)
y = np.array(object=[2, 3, 5, 7], dtype=np.float64)
f = np.polynomial.polynomial.Polynomial.fit(
    x=x, y=y, deg=1, domain=(np.min(x), np.max(x))
)
yf = [f(cx) for cx in x]
fig, ax = plt.subplots()
ax.plot(x, y, "o", label="Puntos dispersos", markersize=10)
ax.plot(x, yf, linestyle="-", label="Recta ajustada")
ax.legend()
plt.savefig("fitted.png")

#!/usr/bin/env python
# -*- coding: utf-8 -*-


anfang, ende = 1, 10
print(r"\begin{tabular}{r|r}")
print(r"$m$ & $2^m$       \\ \hline")
for m in range(anfang, ende + 1):
    print(m, "  & ", 2**m, r" \\")
print(r"\end{tabular}")

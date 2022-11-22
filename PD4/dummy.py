#!/usr/bin/env python

import numpy as np
import scipy as sp


class MMFileFixedFormat(sp.io.mmio.MMFile):
    def _field_template(self, field, precision):
        # Override MMFile._field_template.
        return f"%.{precision}f\n"


A = np.array(
    object=[
        [4, -1, 0, -1, 0, 0],
        [-1, 4, -1, 0, -1, 0],
        [0, -1, 4, 0, 0, -1],
        [-1, 0, 0, 4, -1, 0],
        [0, -1, 0, -1, 4, -1],
        [0, 0, -1, 0, -1, 4],
    ],
    dtype=np.float64,
)
b = np.array(object=[0, 5, 0, 6, -2, 6], dtype=np.float64)
# Save as csv
np.savetxt(fname="A.csv", X=A, fmt="%i", delimiter=",")
np.savetxt(fname="b.csv", X=b, fmt="%i", delimiter=",")
# np.savetxt(fname="foo.csv", X=A, fmt="%.2f", delimiter=",")

# Save as matrix market
MMFileFixedFormat().write("matrix.mtx", a=A, precision=9)
A_out = sp.io.mmread("matrix.mtx")
print(type(A_out), A_out)
# https://stackoverflow.com/a/64749997
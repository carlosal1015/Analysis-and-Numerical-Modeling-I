#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import accumulate
import numpy as np


def second_differences(xs, *, direction):
    """Compute second differences. Returns three numpy arrays: the first
    and second differences, as well as a truncated version of the input
    array so that the positions at each index match up.
    """
    xs = np.array(xs)
    if direction == "forward":
        trunc_xs = xs[:-2]
        dxs = xs[1:] - xs[:-1]
        d2xs = dxs[1:] - dxs[:-1]
        return trunc_xs, dxs[:-1], d2xs
    elif direction == "central":
        trunc_xs = xs[1:-1]
        dxs = (xs[2:] - xs[:-2]) / 2
        d2xs = xs[2:] - 2 * xs[1:-1] + xs[:-2]
        return trunc_xs, dxs, d2xs
    else:
        raise NotImplementedError("direction must be forward or central")


def accelerate(xs, **kwargs):
    iterations = kwargs.pop("iterations", 1)
    direction = kwargs.setdefault("direction", "forward")
    strength = kwargs.setdefault("strength", 1)

    if not isinstance(iterations, int) or iterations < 1:
        raise TypeError("The number of iterations must be a positive integer.")

    if iterations > 1:
        return accelerate(accelerate(xs, **kwargs), iterations=iterations - 1, **kwargs)

    xs, dxs, d2xs = second_differences(xs, direction=direction)
    correction = np.where((dxs == 0) & (d2xs == 0), 0, np.divide(dxs**2, d2xs))
    return xs - strength * correction


iterates = list(accumulate(range(5), lambda x, _: 0.5 * (x + 2 / x), initial=1))
acc = accelerate(iterates)
print(acc)

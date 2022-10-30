#!/usr/bin/env -S octave -qf

fprintf('Pregunta N°16\n')
A16 = ones(3);
[L16, T16, P16] = ParlettReid(A16);
left_16 = P16 * A16 * P16'
right_16 = L16 * T16 * L16'
norm(left_16 - right_16);
P16
L16
T16

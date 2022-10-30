#!/usr/bin/env -S octave -qf

fprintf('Pregunta N°14\n')
A14 = [
    1 10 20;
    10 1 30;
    20 30 1
    ];
[L14, T14, P14] = ParlettReid(A14);
left_14 = P14 * A14 * P14';
right_14 = L14 * T14 * L14';
norm(left_14 - right_14);
P14
T14
L14
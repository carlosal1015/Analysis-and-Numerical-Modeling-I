#!/usr/bin/env -S octave -qf

fprintf('Pregunta N°13\n')
A13 = [
    0 1 2 3;
    1 2 2 2;
    2 2 3 3;
    3 2 3 4
    ];
[L13, T13, P13] = ParlettReid(A13);
left_13 = P13 * A13 * P13';
right_13 = L13 * T13 * L13';
norm(left_13 - right_13);
P13
L13
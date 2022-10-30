#!/usr/bin/env -S octave -qf

fprintf('Pregunta N°12\n')
A12 = [
    1 4 2 3;
    4 27 16 13;
    2 16 10 7;
    3 13 7 7
    ];
[L12, T12, P12] = ParlettReid(A12);
left_12 = P12 * A12 * P12'
right_12 = L12 * T12 * L12'
norm(left_12 - right_12);
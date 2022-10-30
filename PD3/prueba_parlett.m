#!/usr/bin/env -S octave -qf

% https://www.cs.cornell.edu/cv/GVL4/M-Files/Chapter%204/Chap4.htm

n = 3;
A = ones(n);

[L, T, P] = ParlettReid(A);
clc
fprintf('Parlett-Reid Factorization\n\n')
A
P
L
T
resultado_1 = P * A * P'
resultado_2 = L * T * L'

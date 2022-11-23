#!/usr/bin/env -S octave -qf

clc
clear all

A = [
    4, 3, 0;
    3, 4, -1;
    0, -1, 4
    ];
b = [24, 30, -24]';
x = [3, 4, -5]';
omega = 1.25;
x_0 = [1, 1, 1]';
N = 15;
tol = 0.00001;

delta = 0.1;

for omega = 1 + delta:0.1:2 - delta
    disp(omega)
    [respuesta, iteraciones] = SOR(A, b, x_0, N, tol, omega)
end

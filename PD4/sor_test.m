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
N = 13;
tol = 0.00001;

[respuesta, iteraciones] = SOR_HW(A, b, x_0, N, tol, omega)

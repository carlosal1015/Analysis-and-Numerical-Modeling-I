clear all
clc

A = ones(3, 3)

[L, T, P] = ParlettReid(A);
clc

fprintf('A\n'), disp(A)
fprintf('P\n'), disp(P)
fprintf('L\n'), disp(L)
fprintf('T\n'), disp(T)
fprintf('||PAP - LTL||=%10.3e\n', norm(P * A * P' - L * T * L'))

#!/usr/bin/env -S octave -qf

% Copyright (C) 2022 Carlos Aznarán <caznaranl@uni.pe>


% This file is part of https://github.com/carlosal1015/Analysis-and-Numerical-Modeling-I .
% https://github.com/carlosal1015/Analysis-and-Numerical-Modeling-I is free software: you can redistribute it and/or modify
% it under the terms of the GNU General Public License as published by
% the Free Software Foundation, either version 2 of the License, or
% (at your option) any later version.

% https://github.com/carlosal1015/Analysis-and-Numerical-Modeling-I is distributed in the hope that it will be useful,
% but WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
% GNU General Public License for more details.

% You should have received a copy of the GNU General Public License
% along with https://github.com/carlosal1015/Analysis-and-Numerical-Modeling-I .  If not, see <http://www.gnu.org/licenses/>.

fprintf('Pregunta N°4b\n')
A = [1 1 3 2; 1 2 1 1; 3 1 1 2; 2 1 2 3];
[L, T, P] = ParlettReid(A);
left_hand_side = P * A * P';
fprintf('P * A * Pt\n')
left_hand_side
right_hand_side = L * T * L';
fprintf('L * T * Lt\n')
right_hand_side
norm(left_hand_side - right_hand_side);
P
L
T

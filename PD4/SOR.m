function [x, iter] = SOR(a, b, x0, nmax, toll, omega)
    format long;
    n = length(a);
    iter = 0;
    r = b - a * x0;
    r0 = norm(r);
    err = norm(r);
    xold = x0;

    while err > toll & iter < nmax
        iter = iter + 1

        for i = 1:n
            s = 0;

            for j = 1:i - 1
                s = s + a(i, j) * x(j);
            end

            for j = i + 1:n
                s = s + a(i, j) * xold(j);
            end

            x(i) = omega * (b(i) - s) / a(i, i) + (1 - omega) * xold(i);

            %if norm(x - x_0) < tol
            %    break;
            %end
        end

        x = x';
        xold = x;
        r = b - a .* x;
        err = norm(r) / r0;
    end

end

function p = newton(f, df, p0, TOL, N)
    p(1) = p0;
    tol(1) = 0;
    i = 1;
    while i <= N
        p(i+1) = p(i) - f(p(i))/df(p(i));
        tol(i+1) = abs(p(i+1) - p(i));
        if tol(i+1) < TOL
            break;
        end
        i = i+1;
    end
    fprintf('x = %10.10f with error = %10.10f\n %i iterations\n\n', p(i+1), tol(i+1), i)
end
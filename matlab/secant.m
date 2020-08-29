function p = secant(f, p0, p1, TOL, N)
    p = [p0, p1];
    fp = [f(p0), f(p1)];
    tol = [0, p1-p0];
    i = 2;
    while i <= N
        p(i+1) = p(i) - fp(i)*(p(i)-p(i-1))/(fp(i)-fp(i-1));
        fp(i+1) = f(p(i+1));
        tol(i+1) = abs(p(i+1) - p(i));
        if tol(i+1) < TOL
            break;
        end
        i = i+1;
    end
    fprintf('x = %10.10f with error = %10.10f\n %i iterations\n\n', p(i+1), tol(i+1), i)
end
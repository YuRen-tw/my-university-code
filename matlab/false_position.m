function p = false_position(f, p0, p1, TOL, N)
    p = [p0, p1];
    fp = [f(p0), f(p1)];
    tol = [0, p1-p0];
    r_p = p;
    r_fp = fp;
    i = 2;
    while i <= N
        p(i+1) = r_p(2) - r_fp(2)*(r_p(2)-r_p(1))/(r_fp(2)-r_fp(1));
        fp(i+1) = f(p(i+1));
        tol(i+1) = abs(p(i+1) - r_p(2));
        if tol(i+1) < TOL
            break;
        end
        if fp(i+1) * r_fp(2) < 0
            r_p(1) = r_p(2);
            r_fp(1) = r_fp(2);
        end
        r_p(2) = p(i+1);
        r_fp(2) = fp(i+1);
        i = i+1;
    end
    fprintf('x = %10.10f with error = %10.10f\n %i iterations\n\n', p(i+1), tol(i+1), i)
end
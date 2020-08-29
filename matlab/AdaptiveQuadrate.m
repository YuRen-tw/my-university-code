function result = AdaptiveQuadrate(f, a, b, TOL, N)
    h = (b - a) / 2;
    fa = f(a);
    fc = f(a + h);
    fb = f(b);
    S = (fa + 4*fc + fb) * h / 3;
    result = RecurrAQ(f, a, h, fa, fc, fb, S, TOL, N);
end

function result = RecurrAQ(f, a, h, fa, fc, fb, S, TOL, N)
    %  a -- d -- c -- e -- b
    fd = f(a + h/2);
    fe = f(a + h*3/2);
    S1 = (fa + 4*fd + fc) * h / 6;
    S2 = (fc + 4*fe + fd) * h / 6;
    if abs(S1 + S2 - S) < TOL || N == 0
        result = S1 + S2;
    else
        L = RecurrAQ(f,   a, h/2, fa, fd, fc, S1, TOL/2, N-1);
        R = RecurrAQ(f, a+h, h/2, fc, fe, fb, S2, TOL/2, N-1);
        result = L + R;
    end
end

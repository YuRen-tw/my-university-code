function result = Simpson(f, a, b)
    c = (a + b) / 2;
    h = (b - a) / 2;
    result = (h/3) * (f(a) + 4*f(c) + f(b));
end
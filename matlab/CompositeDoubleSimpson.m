function result = CompositeDoubleSimpson(f, ya, yb, a, b, xN, yN)
    F = @(x) CompositeSimpson(@(y)f(x,y), ya(x), yb(x), yN);
    result = CompositeSimpson(F, a, b, xN);
end

function result = CompositeSimpson(f, a, b, N)
    h = (b - a) / (2 * N);
    result = f(a) - f(b);
    % Since the result will += 2*f(b) in the final step of the following loop.
    Cs = 0; Rs = 0;
    for j = 1:N
        Cs = Cs + f(a + h * (2*j-1));
        Rs = Rs + f(a + h * 2*j);
    end
    result = (h/3) * (result + 4*Cs + 2*Rs);
end
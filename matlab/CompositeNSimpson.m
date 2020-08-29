function result = CompositeNSimpson(f, A, B, N)
    n = length(A);
    F = @(X) f(X{:});
    for j = n:-1:2
        Aj = A{j};
        Bj = B{j};
        F = @(X) CompositeSimpson(@(y)F([X,{y}]), Aj(X{:}), Bj(X{:}), N{j});
    end
    result = CompositeSimpson(@(x)F({x}), A{1}, B{1}, N{1});
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

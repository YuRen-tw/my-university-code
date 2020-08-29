function R = RombergIntegration(f, a, b, N)
    R = zeros(N, N);
    R(1,1) = Trapezoidal(f, a, b);
    h = b - a;
    for k = 2:N
        h = h / 2;
        R(k,1) = nextTrapezoidal(f, a, h, R(k-1,1), k);
        for j = 2:k
            R(k,j) = R(k,j-1) + (R(k,j-1) - R(k-1,j-1)) / (4^(j-1)-1);
        end
    end
end

function result = nextTrapezoidal(f, a, h, prevT, k)
    Sig = @(j) f(a + h*(2*j-1));
    result = (prevT + bigsum(1, 2^(k-2), Sig) * h * 2) / 2;
end

function result = Trapezoidal(f, a, b)
    result = (b-a) * (f(a) + f(b)) / 2;
end

function result = bigsum(a, b, f)
    result = sum(arrayfun(f, a:b));
end

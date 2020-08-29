function result = RungeKutta4(f, c, a, b, N)
    h = (b - a) / N;
    t = a;
    w = c;
    result = zeros(N+1, 2);
    result(1,:) = [t, w];
    for j = 1:N
        K1 = h * f(t, w);
        K2 = h * f(t + h/2, w + K1/2);
        K3 = h * f(t + h/2, w + K2/2);
        K4 = h * f(t + h, w + K3);
        w = w + (K1 + K2*2 + K3*2 + K4) / 6;
        t = t + h;
        result(j+1,:) = [t, w];
    end
end
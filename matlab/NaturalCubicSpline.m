function result = NaturalCubicSpline(X, Y)
    X = X(1,:); Y = Y(1,:);
    if length(X) ~= length(Y)
        error('input vectors must have the same length')
    end
    n = length(X);
    dX = zeros(1, n-1);
    for i = 1 : n-1
        dX(i) = X(i+1) - X(i);
    end
    aj = Y;
    A = zeros(n);
    A(1,1) = 1;
    A(n,n) = 1;
    for i = 2 : n-1
        A(i,i-1) = dX(i-1);
        A(i,i) = 2*(dX(i-1) + dX(i));
        A(i,i+1) = dX(i);
    end
    b = zeros(n, 1);
    for i = 2 : n-1
        b(i) = (3/dX(i)) * (aj(i+1)-aj(i)) - (3/dX(i-1)) * (aj(i)-aj(i-1));
    end
    cj = Algorithm_6_7(A, b);
    bj = zeros(1, n); dj = zeros(1, n);
    for i = 2: n
        j = n-i+1;
        bj(j) = (aj(j+1) - aj(j))/dX(j) - dX(j)*(cj(j+1) + 2*cj(j))/3;
        dj(j) = (cj(j+1) - cj(j)) / (3*dX(j));
    end
    result = [aj', bj', cj', dj'];
end


function x = Algorithm_6_7(A, b)
    n = length(A);
    L = zeros(n); U = zeros(n); z = zeros(1, n);
    for i = 1 : n
        U(i,i) = 1;
    end
    L(1,1) = A(1,1);
    U(1,2) = A(1,2) / L(1,1);
    z(1) = b(1) / L(1,1);
    for i = 2 : n-1
        L(i,i-1) = A(i,i-1);
        L(i,i) = A(i,i) - L(i,i-1)*U(i-1,i);
        U(i,i+1) = A(i,i+1) / L(i,i);
        z(i) = (b(i) - L(i,i-1)*z(i-1)) / L(i,i);
    end
    L(n,n-1) = A(n,n-1);
    L(n,n) = A(n,n) - L(n,n-1)*U(n-1,n);
    z(n) = (b(n) - L(n,n-1)*z(n-1)) / L(n,n);
    x(n) = z(n);
    for i = 1 : n-1
        j = n-i;
        x(j) = z(j) - U(j,j+1)*x(j+1);
    end
end
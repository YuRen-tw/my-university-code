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
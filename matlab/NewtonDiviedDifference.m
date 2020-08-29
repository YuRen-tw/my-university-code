function result = NewtonDiviedDifference(X, Y)
    X = X(1,:); Y = Y(1,:);
    if length(X) ~= length(Y)
        error('input vectors must have the same length')
    end
    n = length(X);
    result = zeros(n);
    result(:,1) = Y';
    for c = 2 : n
        for r = 1 : (n-c+1)
            result(r,c) = (result(r+1,c-1) - result(r,c-1)) / (X(r+c-1) - X(r));
        end
    end
end
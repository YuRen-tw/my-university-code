function result = NumDiff(Y, X, ith, pt, direct, step)
    % NumDiff(Y, X, ith [, pt, direct, step])
    %   Compute f'(x_i).
    %
    % Parameters:
    %   Y      : Y = [y_1 ... y_n] = [f(x_1) ... f(x_n)]
    %   X      : one of the following
    %       1) X = [x_1 ... x_n] (must be increasing)
    %       2) X = x_2 - x_1
    %   ith    : the index of x_i
    %   pt     : 3 or 5, 3-point or 5-point methods
    %   direct : 0 (midpoint), 1 (forward endpoint), -1 (backward endpoint)
    %   step   : step > 0, increment between indices of points
    %                                   1 2 3 4 5 6
    %   NumDiff(1:6, X, 3)          : [ o o x o o - ]
    %   NumDiff(1:6, X, 2)          : [ o x o - - - ]
    %   NumDiff(1:6, X, 1)          : [ x o o o o - ]
    %   NumDiff(1:6, X, 1, 3)       : [ x o o - - - ]
    %   NumDiff(1:6, X, 3, 3, 1)    : [ - - x o o - ]
    %   NumDiff(1:6, X, 3, 3, 0, 2) : [ o - x - o - ]
    %
    % Examples:
    % >> f = @(x) 2*x^3 + 4*x^2 + 3*x;
    % >> X = 5 + (-2:2) * 0.3;
    % >> Y = arrayfun(f, X);
    % >> NumDiff(Y, X, 3)
    % ans =
    %   193.0000
    
    if all(size(X) == 1)
        dx = X;
    else
        lenX = length(X);
        if lenX ~= length(Y)
            error('Y and X must be same length.');
        end
        dx = X(2) - X(1);
        if dx <= 0
            error('X must be increasing.');
        end
        if any(X(2:lenX) - X(1:lenX-1) - dx >= 1e-5)
            error('X must have the same difference.');
        end
    end
    switch nargin
        case 3
            result = NumDiff_Y(Y, dx, ith);
        case 4
            result = NumDiff_Y(Y, dx, ith, pt);
        case 5
            result = NumDiff_Y(Y, dx, ith, pt, direct);
        otherwise
            result = NumDiff_Y(Y, dx, ith, pt, direct, step);
    end
end

function result = NumDiff_Y(Y, dx, ith, pt, direct, step)
    % Spec:
    %                                  1 2 3 4 5 6
    % NumDiff(1:6, dx, 3)          : [ o o x o o - ]
    % NumDiff(1:6, dx, 2)          : [ o x o - - - ]
    % NumDiff(1:6, dx, 1)          : [ x o o o o - ]
    % NumDiff(1:6, dx, 1, 3)       : [ x o o - - - ]
    % NumDiff(1:6, dx, 3, 3, 1)    : [ - - x o o - ]
    % NumDiff(1:6, dx, 3, 3, 0, 2) : [ o - x - o - ]
    
    if dx <= 0
        error('dx must be positive.');
    end
    
    lenY = length(Y);
    if floor(ith) ~= ith
        error('index must be integer.');
    end
    if (ith < 1) || (lenY < ith)
        error('Index out of range. ( ith=%d not in 1:%d )', ith, lenY);
    end
    
    if nargin < 6
        step = 1;
    end
    if step <= 0
        error('step must be positive.');
    end
    if floor(step) ~= step
        error('step must be integer.');
    end
    
    if nargin < 5
        lpts = ith - 1;
        rpts = lenY - ith;
        if nargin < 4
            if (max([lpts rpts]) >= step*4) || (min([lpts rpts]) >= step*2)
                pt = 5;
            else
                pt = 3;
            end
        end
        
        direct = 0;
        if lpts >= step*2
            direct = direct - 1;
        end
        if rpts >= step*2
            direct = direct + 1;
        end
    end
    if (pt ~= 3) && (pt ~= 5)
        error('Only support 3-point and 5-point methods.');
    end
    if direct ~= 0
        direct = direct / abs(direct);
    end
    
    halfpts = (pt-1) / 2;
    startidx = ith - step * halfpts * (1 - direct);
    endidx   = ith + step * halfpts * (1 + direct);
    
    if (startidx < 1) || (lenY < endidx)
        error('Out of range. ( %d:%d not in 1:%d )', startidx, endidx, lenY);
    end
    Ds = {@D_p3end @D_p3mid @D_p5end @D_p5mid};
    D = Ds{pt - 1 - abs(direct)};
    Y = Y(startidx : step : endidx);
    
    if direct == -1
        result = D(fliplr(Y), -dx * step);
    else
        result = D(Y, dx * step);
    end
end

function result = D_p3end(Y, dx)
    result = (-3*Y(1) + 4*Y(2) - Y(3)) / (2*dx);
end

function result = D_p3mid(Y, dx)
    result = (-Y(1) + Y(3)) / (2*dx);
end

function result = D_p5end(Y, dx)
    result = (-25*Y(1) + 48*Y(2) - 36*Y(3) + 16*Y(4) - 3*Y(5)) / (12*dx);
end

function result = D_p5mid(Y, dx)
    result = (Y(1) - 8*Y(2) + 8*Y(4) - Y(5)) / (12*dx);
end

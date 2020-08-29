%% 4.2  Example 2
% Example of NumDiff

%%
% Values in Table 4.2
X = [1.8 1.9 2.0 2.1 2.2];
Y = [10.889365 12.703199 14.778112 17.148957 19.855030];
% True value of f'(2.0)
F = 22.167168;

%% Show
% Function for print result
printWithErr = @(t, x) fprintf('%s: %f, error = %f\n', t, x, abs(x - F));
%
disp('-----');
printWithErr('Three-point endpoint with h= 0.1', NumDiff(Y, X, 3, 3, 1));
printWithErr('Three-point endpoint with h=-0.1', NumDiff(Y, X, 3, 3, -1));
printWithErr('Three-point midpoint with h= 0.1', NumDiff(Y, X, 3, 3));
printWithErr('Three-point midpoint with h= 0.2', NumDiff(Y, X, 3, 3, 0, 2));
printWithErr(' Five-point midpoint with h= 0.1', NumDiff(Y, X, 3));
disp('-----');

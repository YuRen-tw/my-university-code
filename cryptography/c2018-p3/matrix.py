import itertools as it
import numpy as np
import MRT_name

Matrix = np.matrix
det = np.linalg.det
inv = np.linalg.inv
'''
# matrix:
np.matrix([[a, b, c],
           [d, e, f],
           [g, h, i]])

# det:
np.linalg.det(M)

# inv
np.linalg.inv(M)
'''

abcs = [chr(n) for n in range(ord('a'), ord('z')+1)]
primes = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
inv_primes = [1, 9, 21, 15, 3, 19, 7, 23, 11, 5, 17, 25]

def inv_prime(p):
    return inv_primes[primes.index(p)]
    
def abc2num(a):
    return abcs.index(a) if a.isalpha() else 0
def num2abc(n):
    return abcs[n % 26]

def group(n, xs):
    return list(zip(*([iter(xs)]*n)))
def ungroup(xss):
    return [x for xs in xss for x in xs]


def Mx3(M, xs):
    num_xs = map(abc2num, xs)
    M = Matrix(M)
    X = Matrix(group(3, num_xs)).transpose()
    num_ys = ungroup((M * X).transpose().tolist())
    ys = ''.join(num2abc(round(i)) for i in num_ys)
    return ys

def inputMatrixGen():
    cell = []
    for row in range(3):
        for col in input('_ _ _ : ').split():
            if col.isnumeric():
                cell.append([int(col)])
            else:
                cell.append(range(26))
    return (Matrix(group(3, c)) for c in it.product(*cell))

def find(ys):
    ys = ys.lower()
    for M in inputMatrixGen():
        detM = round(det(M))
        if detM % 26 not in primes:
            continue
        invM = inv(M) * detM * inv_prime(detM % 26)
        xs = Mx3(invM, ys)
        for name, zh_name in MRT_name.station_name:
            if name in xs:
                print(xs, zh_name)
                print(M)

def test(n):
    a = Matrix([[1,2,3],[4,5,6],[7,8,0]])
    station = MRT_name.station_name[n][0]
    r = (3 - len(station) % 3) % 3
    if r:
        station = station + 'o' * r
    m = Mx3(a, station)
    print(': {}'.format(m))
    find(m)


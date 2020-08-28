import axb_MRT_name

abcs = [chr(n) for n in range(ord('a'), ord('z')+1)]
primes = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
inv_primes = [1, 9, 21, 15, 3, 19, 7, 23, 11, 5, 17, 25]

def inv_prime(p):
    return inv_primes[primes.index(p)]
    
def abc2num(a):
    return abcs.index(a) if a.isalpha() else 0
def num2abc(n):
    return abcs[n % 26]

def compute(f, xs):
    num_xs = map(abc2num, xs)
    num_ys = map(f, num_xs)
    return ''.join(map(num2abc, num_ys))

def axb(xs, a, b):
    f = lambda n: (a * n + b) % 26 
    return compute(f, xs)

def inv_axb(xs, a, b):
    f = lambda n: (n + 26 - b) * inv_prime(a)
    return compute(f, xs)

def find(ys):
    ys = ys.lower()
    for axb_name, zh_name, a, b in axb_MRT_name.station_name:
        if axb_name in ys:
            xs = inv_axb(ys, a, b)
            print(xs, zh_name, a, b)


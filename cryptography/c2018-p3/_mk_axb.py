import MRT_name

abcs = [chr(n) for n in range(ord('a'), ord('z')+1)]
primes = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

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

# make file
print('station_name = [')
for en_name, zh_name in MRT_name.station_name:
    for a, b in ((x,y) for x in prime for y in range(26)):
        axb_name = axb(en_name, a, b)
        print("    ('{}', '{}', {}, {}),".format(axb_name, zh_name, a, b))
print(']')

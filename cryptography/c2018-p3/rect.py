import MRT_name

def jojoin(xss):
    return ''.join(''.join(xs) for xs in xss)

def rect(xs, n):
    return jojoin(xs[j] for i in range(n) for j in range(i, len(xs), n))

def inv_rect(xs, n):
    return rect(xs, len(xs)//n)

def factor(n): return (i for i in range(2,n) if n%i == 0)

def find(ys):
    ys = ys.lower()
    for n in factor(len(ys)):
        xs = inv_rect(ys, n)
        for name, zh_name in MRT_name.station_name:
            if name in xs:
                print(xs, zh_name, n)


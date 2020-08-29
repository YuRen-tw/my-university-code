primes_26 = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
inv_primes_26 = [1, 9, 21, 15, 3, 19, 7, 23, 11, 5, 17, 25]

def ab_pair_26():
    yield from ((a,b) for a in primes_26 for b in range(26))

def inv_prime_26(p):
    return inv_primes_26[primes_26.index(p)]

def axb_26(a, b, inv=False):
    if inv:
        return lambda x: (x - b) * inv_prime_26(a) % 26
    return lambda x: (a * x + b) % 26



# Factorization

'''
def natural_numbers(start=0, step=1):
    i = start
    while True:
        yield i
        i += step

_PRIMES = [2, 3]
def primes():
    yield from _PRIMES
    for n in natural_numbers(_PRIMES[-1]+2, 2):
        if isprime(n):
            yield n
            _PRIMES.append(n)

def least_prime_factor(n):
    for p in primes():
        if p ** 2 > n:
            break
        if n % p == 0:
            return p
    return n

def isprime(n):
    if n <= 2:
        return n == 2
    return least_prime_factor(n) == n

def factorize(n):
    result = {}
    while n != 1:
        p = least_prime_factor(n)
        n //= p
        if p not in result:
            result[p] = 1
        else:
            result[p] += 1
    return result
'''
# I give up :/

import maxima_interface as Maxima

isprime = Maxima.primep
factorize = Maxima.factor
next_prime = Maxima.next_prime


# Ch'in Chiu-shao: Ta-yan Ch'iu-yi Shu
def modular_inverse(a, m):
    "Return modular inverse of a mod m. (0 if a and m are not coprime)"
    LT, LB, Chi, Ting = 1, 0, a, m
    while True:
        RB = Ting // Chi
        LB += LT * RB
        Ting -= Chi * RB
        if Ting == 0:
            return LT if Chi == 1 else 0
        RT = (Chi-1) // Ting
        LT += LB * RT
        Chi -= Ting * RT


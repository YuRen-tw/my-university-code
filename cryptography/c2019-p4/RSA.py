import random
import num_theory


def blocks_modpow(blocks, power, modulus):
    return [pow(num, power, modulus) for num in blocks]


def abc2num(a):
    return ord(a) - ord('a')

def num2abc(n):
    return chr(n % 26 + ord('a'))

def text2blocks(text, term_size, fill='x'):
    padding = (term_size - len(text) % term_size) % term_size
    if padding:
        text = text + fill * padding
    # text      = 'xyzabc'
    # terms     = 'xy' 'za' 'bc'
    # preblocks = ('23' '24') ('25' '01') ('02' '03')
    # blocks    = [2324, 2501, 203]
    terms = (text[i:i+term_size] for i in range(0, len(text), term_size))
    preblocks = ((str(abc2num(c)).rjust(2,'0') for c in cs) for cs in terms)
    blocks = [int(''.join(block)) for block in preblocks]
    return blocks

def blocks2text(blocks, term_size):
    size = term_size * 2
    # blocks = [2324, 2501, 203]
    # strs   = '2324' '2501' '0203'
    # nums   = 23 24 25 1 2 3
    # text   = 'xyzabc'
    strs = (str(num).rjust(size, '0') for num in blocks)
    nums = (int(s[i:i+2]) for s in strs for i in range(0, size, 2))
    text = ''.join(num2abc(n) for n in nums)
    return text


def mkRSAkeys(p, q, e):
    #if not num_theory.isprime(p) or not num_theory.isprime(q) or p == q:
    #    raise ValueError('p and q must be two distinct primes')
    N = p * q
    r = (p-1) * (q-1)
    if e >= r:
        raise ValueError('e must be less than (p-1)(q-1)')
    d = num_theory.modular_inverse(e, r)
    if d == 0:
        raise ValueError('e and (p-1)(q-1) must be coprime')
    pubkey = (N, e)
    privkey = (N, d)
    return pubkey, privkey

def _maxlen(N):
    s = str(N)
    maxlen = len(s) // 2
    if s[-2*maxlen:] <= '25' * maxlen:
        maxlen -= 1
    return maxlen

def RSAencipher(text, N, e, fill='x'):
    length = _maxlen(N)
    blocks = text2blocks(text, length, fill)
    result = blocks_modpow(blocks, e, N)
    return result

def RSAdecipher(blocks, N, d):
    length = _maxlen(N)
    result = blocks_modpow(blocks, d, N)
    return blocks2text(result, length)


def mk_random_prime():
    return num_theory.next_prime(random.randrange(2e15, 2e16))

def mk_random_e(p, q):
    r = (p-1) * (q-1)
    valid = False
    while not valid:
        e = random.randrange(3, r//200)
        valid = num_theory.modular_inverse(e, r) != 0
    return e

def test():
    text = 'thequickbrownfoxjumpsoverthelazydog'
    p = mk_random_prime()
    q = mk_random_prime()
    e = mk_random_e(p, q)
    pubkey, privkey = mkRSAkeys(p, q, e)
    cipher = RSAencipher(text, *pubkey)
    
    print('p={}, q={}'.format(p, q))
    print('pubkey={}, privkey={}'.format(pubkey, privkey))
    print('{} => {}'.format(text, cipher))


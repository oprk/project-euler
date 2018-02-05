# Prime pair sets
# Problem 60

# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes
# and concatenating them in any order the result will always be prime. For
# example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four
# primes, 792, represents the lowest sum for a set of four primes with this
# property.

# Find the lowest sum for a set of five primes for which any two primes
# concatenate to produce another prime.

import time

def sieve(limit):
    yield 2
    np = set()
    for x in range(3, limit, 2):
        if x in np:
            continue
        yield x
        np.update(range(x + x, limit, x))


_known_primes = set(sieve(100))


# Modified Miller-Rabin algorithm
def is_prime(n, k=16):
    if n < 2:
        return False
    if n in _known_primes:
        return True
    for p in _known_primes:
        if n % p == 0:
            return False
    d, s = n - 1, 0
    while d & 1 == 0:
        d, s = (d >> 1, s + 1)

    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    for a in (2, 3):
        if pow(a, d, n) == 1:
            continue
        is_composite = True
        for i in range(s):
            if pow(a, (1 << i) * d, n) == n - 1:
                is_composite = False
                break
        if is_composite:
            return False
    return True


def answer():
    primes_with_str = [
        (i, str(p), p)
        for i, p in enumerate(sieve(10000))
    ]
    primes_with_str.pop(0)
    c_able = {
        pa: {
            pb for _, sb, pb in primes_with_str[i:]
            if is_prime(int(sa + sb)) and is_prime(int(sb + sa))
        }
        for i, sa, pa in primes_with_str
    }
    return next(
        pa + pb + pc + pd + pe
        for pa, ca in ((pa, c_able[pa]) for pa in c_able)
        for pb, cab in ((pb, ca.intersection(c_able[pb])) for pb in ca)
        for pc, cabc in ((pc, cab.intersection(c_able[pc])) for pc in cab)
        for pd, cabcd in ((pd, cabc.intersection(c_able[pd])) for pd in cabc)
        for pe in cabcd
    )

t0 = time.time()
result = answer()
t1 = time.time()
print(result)
print('time: %f' % (t1 - t0))
# 26033
# time: 1.881190

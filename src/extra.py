def mobius_range(n, primes):
    """Computes Möbius function for 0 to n using sieve approach.

    Requires `primes` to contain all primes below n.
    https://mathoverflow.net/a/200392
    """
    mus = [1] * (n+1)
    mus[0] = 0
    for p in primes:
        if p > n: break
        for i in range(p, n+1, p):
            mus[i] *= -1
        for i in range(p**2, n+1, p**2):
            mus[i] = 0

    return mus



def ternary_search(f, l, r):
    for i in range(100):
        m1 = l + (r-l) // 3
        m2 = r - (r-l) // 3
        #print(l, m1, m2, r)

        if f(m1) < f(m2):
            r = m2
        else:
            l = m1
    return (l + r) // 2

from functools import cache

@cache
def c(s, d):
    """Count integers with d digits and s digit-sum"""
    if s < 0: return 0
    assert d >= 0
    if d == 0: return int(s == 0)
    return sum(c(s-i, d-1) for i in range(10))

@cache
def D(s,d):
    """Sum of integers with d digits and s digit-sum"""
    if s <= 0: return 0
    if d == 0: return 0
    assert d >= 0
    return sum(i * c(s-i, d-1) * 10**(d-1) + D(s-i, d-1) for i in range(10))


def partitions(n, m=1):
    """Create partitions of n.

    :param n: integer to partition
    :param m: min new value to add (for recursion)
    :return: generator of ordered partitions, e.g. [1,1,1], [1,2], [3]
    """
    if n == 0:
        yield []
        return

    for i in range(m, n+1):
        for l in partitions(n-i, i):
            yield [i] + l


def comb_mod(n, k, m):
    from number import mod_inv
    assert n >= 0
    num, den = 1, 1
    for i in range(n-k+1, n+1):
        num = (num * i) % m
    for i in range(1, k+1):
        den = (den * i) % m

    return (num * mod_inv(den, m)) % m


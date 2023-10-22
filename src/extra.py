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